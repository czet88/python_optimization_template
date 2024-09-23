from src.instance_manager import InstanceManager

if __name__ == "__main__":
    parameters = {
        "path_to_dir": "local_path",
        "solvers": ["MIP"]
    }

    instance_manager = InstanceManager(parameters.get("path_to_dir"))
    top_solutions = instance_manager.solve(parameters.get("solvers"), 3)
