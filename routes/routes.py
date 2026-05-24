from fastapi import APIRouter
from utils.commands import  execute_linux_command

router = APIRouter(prefix="/system")

@router.get("/uptime")
def uptime():
    return execute_linux_command(["uptime"])

@router.get("/whoami")
def whoami():
    return execute_linux_command(["whoami"])

@router.get("/disk")
def disk():
    return execute_linux_command(["df", "-h"])


@router.get("/memory")
def memory():
    return execute_linux_command(["free", "-m"])

@router.get("/test-error")
def test_error():
    return execute_linux_command(["wrongcommand"])
