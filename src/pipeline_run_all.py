import sys
import traceback
from datetime import datetime

from src.ingestion.stage1_pipeline import run_stage1
from src.enrichment.stage2_pipeline import run_stage2
from src.scoring.stage3_pipeline import run_stage3

def log(msg: str):
    """Simple timestamped logger"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def run_all():
    log("Starting Lead Generation and Ranking Pipeline")
    try:
        log("Stage 1: Identification Started")
        run_stage1()

        log("Stage 2: Enrichment Started")
        run_stage2()

        log("Stage 3: Ranking Started")
        run_stage3()

        log("Pipeline Completed Successfully")
    except Exception as e:
        log("Pipeline Failed")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    run_all()