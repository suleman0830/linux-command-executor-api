import subprocess


def execute_command(command):
    
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        return {"output": result.stdout.splitlines()}
    
    except subprocess.CalledProcessError as e:
        return {
            "success": False,
            "error": e.stderr.strip()
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
        