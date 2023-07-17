# Rhino-Hops-Backend

This repository makes it possible to run Grasshopper definitions through a local Rhino-Compute instance. 

This can be extremely useful to execute definitions very quickly, automate Grasshopper workflows, or integrate Grasshopper scripts into existing workflows. 🚀🌱

To run your own Rhino Compute instance and start executing your Grasshopper definitions locally, follow the guide below: 

## Requirements:
- 💻 Windows PC
- 🦏 Rhino 7
- 🐍 Python =< 3.10

## Steps:
1. Download and install the Hops plugin for Rhino [here](https://developer.rhino3d.com/guides/compute/hops-component/) 
2. Clone this repository and install the virtual environment using Python =< 3.10 (Rhino libraries are not yet compatible with Python 3.11) 
3. Edit your Grasshopper definition so that the Hops 'Get components' are connected to input and output. They can be found under Params Tab > Util Group 
4. Modify the Python code in this repo to match the inputs and outputs of your Grasshopper definition, and update the hardcoded paths 
5. Ensure that Rhino and Grasshopper are open (it is not necessary to open the Grasshopper definition you want to execute) 
6. Run the `main.py` script to execute the definition through Rhino Compute 🚀

![image](https://github.com/yannickmacken/rhino-hops-backend/assets/93203883/e50cb5e6-502f-4246-b8a3-c15ad7e72e48)

## Use Cases:
This solution opens the door to many exciting possibilities. With this method, you can integrate Grasshopper into existing Python workflows, call Grasshopper instances on a remote server from a client app, or easily automate complex workflows with multiple Grasshopper files. Happy coding! 😊🎉
