import re
import numpy as np

def parse_log_file(file_path):
    net_worths = []
    daily_returns = []

    with open(file_path, 'r') as file:
        for line in file:
            # Capture net worth
            nw_match = re.search(r"'net_worth': ([\d\.eE\+\-]+)", line)
            if nw_match:
                net_worths.append(float(nw_match.group(1)))
            # Capture daily return
            roi_match = re.search(r"'today_roi': ([\d\.eE\+\-]+)", line)
            if roi_match:
                daily_returns.append(float(roi_match.group(1)))

    if not net_worths:
        raise ValueError("No net worth data found in the log file.")

    # Calculate total return
    initial_net_worth = net_worths[0]
    final_net_worth = net_worths[-1]
    total_return = ((final_net_worth - initial_net_worth) / initial_net_worth) * 100

    print(f"Initial net worth: {initial_net_worth}")
    print(f"Final net worth: {final_net_worth}")

    # Calculate daily return statistics
    daily_returns = np.array(daily_returns) * 100
    print(f"Daily returns: {daily_returns.shape}")

    mean_daily_return = np.mean(daily_returns)
    std_daily_return = np.std(daily_returns)

    # Calculate Sharpe ratio (assuming risk-free rate = 0)
    sharpe_ratio = mean_daily_return / std_daily_return if std_daily_return != 0 else float('-inf')

    return {
        "Total Return": total_return,
        "Mean Daily Return": mean_daily_return,
        "Sharpe Ratio": sharpe_ratio
    }

# Example usage:
log_file_path = "./logs/btc-sideways.out"  # Replace with actual path
results = parse_log_file(log_file_path)
print(results)
