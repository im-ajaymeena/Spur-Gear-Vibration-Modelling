
# Build docker image
docker build -t ode_solver .

# Run docker image
bash ./run.sh 

### to set parameters use params1.py, all the paameters from it then imported inside ODE_solver.py
some of the parameters
total_time: time duration for which the model has to be estimated. If time is increased it would take longer to solve differential equation. 
