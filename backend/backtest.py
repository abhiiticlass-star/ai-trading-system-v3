def backtest(data, model):

    wins = 0
    losses = 0

    for i in range(20, len(data)-1):

        features = data.iloc[i][["body","range","trend","momentum"]].values
        signal = model.predict([features])[0]

        if signal == 1 and data.iloc[i+1]["close"] > data.iloc[i]["close"]:
            wins += 1
        else:
            losses += 1

    return {
        "wins": wins,
        "losses": losses,
        "accuracy": wins / (wins + losses)
    }
