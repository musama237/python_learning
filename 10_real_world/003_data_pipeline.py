"""
Challenge: Data Pipeline Framework
Difficulty: ⭐⭐⭐ Hard
Topic: ETL, Pipeline Pattern, Data Processing

Build a composable data pipeline framework for ETL operations.

Hints:
    1. Store steps as list of Step objects
    2. run() loops through steps passing data forward
    3. Wrap each step in try/except
    4. error_handler receives (exception, current_data) and returns recovery data
"""

from typing import Any, Callable
from dataclasses import dataclass, field
import json
import csv
from io import StringIO
from pathlib import Path


@dataclass
class PipelineResult:
    success: bool
    data: Any = None
    error: str = None
    steps_executed: list[str] = field(default_factory=list)


class Step:
    """A single pipeline step with a name and transform function."""

    def __init__(self, name: str, func: Callable, error_handler: Callable = None):
        # YOUR CODE HERE
        pass

    def execute(self, data: Any) -> Any:
        """Execute step. Use error_handler if provided, else raise."""
        # YOUR CODE HERE
        pass


class DataPipeline:
    """Composable data pipeline.

    Usage:
        pipeline = (DataPipeline("my_pipeline")
                   .add_step("load", load_fn)
                   .add_step("transform", transform_fn)
                   .add_step("validate", validate_fn)
                   .add_step("save", save_fn))
        result = pipeline.run(initial_data)
    """

    def __init__(self, name: str):
        # YOUR CODE HERE
        pass

    def add_step(self, name: str, func: Callable,
                 error_handler: Callable = None) -> "DataPipeline":
        """Add a step. Return self for chaining."""
        # YOUR CODE HERE
        pass

    def run(self, data: Any = None) -> PipelineResult:
        """Execute all steps in order. Return PipelineResult."""
        # YOUR CODE HERE
        pass

    def dry_run(self) -> list[str]:
        """Return list of step names without executing."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    # Test basic pipeline
    pipeline = (DataPipeline("test")
                .add_step("double", lambda x: x * 2)
                .add_step("add_ten", lambda x: x + 10)
                .add_step("to_string", lambda x: str(x)))

    result = pipeline.run(5)
    assert result.success is True
    assert result.data == "20"
    assert result.steps_executed == ["double", "add_ten", "to_string"]

    # Test dry run
    assert pipeline.dry_run() == ["double", "add_ten", "to_string"]

    # Test error handling
    def bad_step(data):
        raise ValueError("Something went wrong")

    error_pipeline = (DataPipeline("error_test")
                      .add_step("ok", lambda x: x + 1)
                      .add_step("fail", bad_step))

    result2 = error_pipeline.run(1)
    assert result2.success is False
    assert "Something went wrong" in result2.error
    assert result2.steps_executed == ["ok"]

    # Test with error handler
    recovered_pipeline = (DataPipeline("recovery")
                          .add_step("fail", bad_step, error_handler=lambda e, d: d)
                          .add_step("continue", lambda x: x * 2))

    result3 = recovered_pipeline.run(5)
    assert result3.success is True
    assert result3.data == 10

    # Test data transformation pipeline
    csv_data = "name,age\nAlice,30\nBob,25"

    transform_pipeline = (DataPipeline("csv_transform")
                          .add_step("parse", lambda d: list(csv.DictReader(StringIO(d))))
                          .add_step("filter", lambda rows: [r for r in rows if int(r["age"]) > 26])
                          .add_step("format", lambda rows: [{"name": r["name"].upper()} for r in rows]))

    result4 = transform_pipeline.run(csv_data)
    assert result4.success is True
    assert result4.data == [{"name": "ALICE"}]
    print("✅ All tests passed!")
