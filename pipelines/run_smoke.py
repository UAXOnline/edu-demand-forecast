from pathlib import Path
import pandas as pd
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.DataFrame(
        [
            {"date": datetime.today().date(), "topic": "ai", "signal": 1.0},
            {"date": datetime.today().date(), "topic": "cyber", "signal": 0.8},
        ]
    )
    out_path = OUT / "smoke_processed.csv"
    df.to_csv(out_path, index=False)
    print(f"[OK] wrote {out_path}")

if __name__ == "__main__":
    main()
