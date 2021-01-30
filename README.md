# Depression Detection on twitter
A project for detecting depression on twitter
## Getting started: 

1. Install the anaconda on your system
2. Install "Git" on your system(windows user should install 'Git bash for windows'). This will help for git version control
3. create a new environment by typing the following cmd: 
```bash
conda env create --name <env_name> -p <project_directory> -f environment.yml
```
This will create a the env with all the dependencies intalled in the new conda env named `twitter`
4. I suggest to use Jupyterlab; as it has useful github extensions especially `Git` for seamless version control and easy collabration

## Project organization

Project organization is based on ideas from [_Good Enough Practices for Scientific Computing_](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510).

1. Put each project in its own directory, which is named after the project.
2. Put external scripts or compiled programs in the `bin` directory.
3. Put raw data and metadata in a `data` directory.
4. Put text documents associated with the project in the `doc` directory.
5. Put all Docker related files in the `docker` directory.
6. Install the Conda environment into an `env` directory. 
7. Put all notebooks in the `notebooks` directory.
8. Put files generated during cleanup and analysis in a `results` directory.
9. Put project source code in the `src` directory.
10. Name all files to reflect their content or function.
