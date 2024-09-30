def identify_candlestick_pattern(data):
    last_candle = data.iloc[-1]

    # Example: Check for a bullish engulfing pattern
    if last_candle['close'] > last_candle['open']:
        previous_candle = data.iloc[-2]
        if previous_candle['close'] < previous_candle['open'] and last_candle['close'] > previous_candle['open'] and last_candle['open'] < previous_candle['close']:
            return "Bullish Engulfing"
    return "No Pattern"
