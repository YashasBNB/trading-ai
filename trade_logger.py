import json
import os

def log_trade(result, parameters):
    log_entry = {
        "result": result,
        "parameters": parameters
    }
    if not os.path.exists('trade_log.json'):
        with open('trade_log.json', 'w') as f:
            json.dump([], f)

    with open('trade_log.json', 'r+') as f:
        logs = json.load(f)
        logs.append(log_entry)
        f.seek(0)
        json.dump(logs, f)

def analyze_trades():
    if not os.path.exists('trade_log.json'):
        print("No trades logged yet.")
        return

    with open('trade_log.json', 'r') as f:
        logs = json.load(f)
    
    wins = sum(1 for log in logs if log['result'] == 'win')
    losses = sum(1 for log in logs if log['result'] == 'loss')
    total = wins + losses
    
    if total == 0:
        print("No trades to analyze.")
        return
    
    win_rate = wins / total * 100
    print(f"Total Trades: {total}, Wins: {wins}, Losses: {losses}, Win Rate: {win_rate:.2f}%")
