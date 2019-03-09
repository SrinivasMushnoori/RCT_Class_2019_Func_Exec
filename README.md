# RCT_Class_2019_Func_Exec
Function Executor project for RCT class 2019.

Software Requirements Document

Requirements
Execute functions concurrently
Must execute from string of functions
“String of functions” refers to how the functions are specified: in our case we go with a “CUD” analogue specified as a dictionary containing the string to be interpreted by exec(), and other details such as resource requirements. 
We assume homogeneity in CU resource requirements
We assume only single core functions
We assume that the functions do not need to communicate.


Design:
exec() to be used
Have an “agent” like architecture that triggers the exec.
Agent: RM, LM, Spawner, Collector
RM: Resource Manager: finds available cores on the remote node, assigns to function CUD’s. 
LM: Launch Method: Essentially exec()
Spawner: The spawner is what triggers exec() to be run on the agent side instance of Python. 
Collector: collect results. Potentially communicate back to Client. Worry about this later.
The RM is extremely important. It has knowledge of available cores and maintains it in a data structure. This data structure will then be used to return lists of currently in-use and available resources. We plan to use the psutil python package. This allows us to retrieve system resource utilization by each process. 
There is a chance that explicit assignments of functions to processes is not required if the OS scheduler is smart enough to schedule only on idle/available cores.
Spawner finds available processes from the RM’s data structure and spawns the workloads accordingly. Processes/functions are pinned to cores to prevent two workloads from being assigned to the same core. 
Core pinning is still being explored. 

General Notes:

[IMPORTANT] Look at core pinning in Python. This is to ensure that no two functions are accidentally assigned to the same core.
We are as of yet unsure how to test scalability of this across multiple nodes. We should be able to make this work across multiple cores, assuming things go according to plan. Across nodes may be somewhat different, i.e. we do not know what to expect. 

Discussion:
Have user put code into function
Utilize eval to import and run main function
Initialize each CU with own interpreter?
