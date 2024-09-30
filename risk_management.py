def risk_management(current_balance, trade_amount):
    risk_limit = current_balance * 0.02  # Risking 2% of balance
    if trade_amount > risk_limit:
        return False
    return True
def risk_management(current_balance, trade_amount):
    risk_limit = current_balance * 0.02  # Risking 2% of balance
    if trade_amount > risk_limit:
        return False
    return True
