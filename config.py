
ROBOT_IP = "10.10.48.252"
ROBOT_PORT = 9559

# checks if naoqi is present
def is_production():
    try:
        __import__("naoqi")
    except ImportError:
        return False
    else:
        return True
