from invoke import Collection

from tasks.lint import lint
from tasks.test import coverage, test
from tasks.typecheck import typecheck
from tasks.verify import verify

namespace = Collection(
    coverage,
    lint,
    test,
    typecheck,
    verify,
)
