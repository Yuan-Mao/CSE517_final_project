# Environment Setup
```
conda env create -f environment.yaml
conda activate cse517_final_project
```

# Run
Execute trading simulation
BTC: 
```
python -u run_agent.py --dataset btc --starting_date 2023-04-12 --ending_date 2023-06-16 &>logs/btc-bear.out 2>&1
python -u run_agent.py --dataset btc --starting_date 2023-06-17 --ending_date 2023-08-25 &>logs/btc-sideways.out 2>&1
python -u run_agent.py --dataset btc --starting_date 2023-10-01 --ending_date 2023-12-01 &>logs/btc-bull.out 2>&1
```

ETH: 
```
python -u run_agent.py --dataset eth --starting_date 2023-04-12 --ending_date 2023-06-16 &>logs/eth-bear.out 2>&1
python -u run_agent.py --dataset eth --starting_date 2023-06-20 --ending_date 2023-08-31 &>logs/eth-sideways.out 2>&1
python -u run_agent.py --dataset eth --starting_date 2023-10-01 --ending_date 2023-12-01 &>logs/eth-bull.out 2>&1
```

SOL:
```
python -u run_agent.py --dataset sol --starting_date 2023-04-12 --ending_date 2023-06-16 &>logs/sol-bear.out 2>&1
python -u run_agent.py --dataset sol --starting_date 2023-07-08 --ending_date 2023-08-31 &>logs/sol-sideways.out 2>&1
python -u run_agent.py --dataset sol --starting_date 2023-10-01 --ending_date 2023-12-01 &>logs/sol-bull.out 2>&1
```

Verify results: `python parse_logs.py`

Run full evaluation: `./run\_agent.sh`
