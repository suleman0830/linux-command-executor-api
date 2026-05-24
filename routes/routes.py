from fastapi import APIRouter
from utils.commands import  execute_command

router = APIRouter(prefix="/system")

@router.get("/uptime")
def uptime():
    command = ["uptime"]
    result = execute_command(command)
    return result

@router.get("/whoami")
def whoami():
    command = ["whoami"]
    result = execute_command(command)
    return result

@router.get("/disk")
def disk():
    return execute_command(["df", "-h"])


@router.get("/memory")
def memory():
    return execute_command(["free", "-m"])

@router.get("/test-error")
def test_error():
    return execute_command(["wrongcommand"])
