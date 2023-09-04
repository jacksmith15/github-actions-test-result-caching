from invoke import task

from tasks.lint import check as lint
from tasks.test import test
from tasks.typecheck import typecheck


@task(post=[lint, typecheck, test])
def verify(_ctx):
    """Run all verification steps."""
