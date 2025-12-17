import sys
import traceback
from datetime import datetime
import argparse
from src.ingestion.stage1_pipeline import run_stage1
from src.enrichment.stage2_pipeline import run_stage2, run_stage2_dummy
from src.scoring.stage3_pipeline import run_stage3

def log(msg: str):
    """Simple timestamped logger"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def run_dummy():
    log("Starting Lead Generation and Ranking Pipeline with Dummy Enrichment (NO PAID APIs)")
    try:
        log("Stage 1: Identification Started")
        run_stage1()

        log("Stage 2: Enrichment Started")
        run_stage2_dummy()

        log("Stage 3: Ranking Started")
        run_stage3()

        log("Pipeline Completed Successfully")
    except Exception as e:
        log("Pipeline Failed")
        traceback.print_exc()
        sys.exit(1)

def run_actual():
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

def main():
    parser = argparse.ArgumentParser(
        description="BD Intelligence Pipeline Runner"
    )

    parser.add_argument(
        "--mode",
        choices=["dummy", "actual"],
        default="dummy",
        help="Run pipeline in dummy mode (no paid APIs) or actual mode"
    )

    args = parser.parse_args()

    try:
        if args.mode == "dummy":
            run_dummy()
        else:
            run_actual()
    except Exception:
        log("Pipeline failed")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()