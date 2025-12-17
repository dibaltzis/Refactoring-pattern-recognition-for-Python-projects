## Helper scripts
- **download_releases_from_github.py**

        - Used to download multiple releases from github.
        - Set the token in the config.py file as described above.
        - Set the maximum number of releases to download in the config.py file as described above.
        - Move the script to the folder you want to download the projects (ex. projects)
        - Modify the list of github urls list inside the file 
        - After the run the outcome will be
            projects
            ├── username_reponame (from the list of github urls)
            |   ├── version_1
            |   └── ...
            ├── username_reponame (from the list of github urls)
            |   ├── version_1
            |   └── ...
            └── config.py
- **run_for_all_the_projects.py**

        - Used to compare multiple projects with multiple versions.
        - Set the project folder path in the config.py file as described above.
            Input folder structure:
                projects
                ├── project_1
                |     ├── version_1
                |     └── ...
                ├── project_2
                |     ├── version_1
                |     └── ...
                └── ...
        - Move the script to the root folder of the project
            Refactoring-recognition-for-python
            ├── Results/
            ├── Documentation/
            ├── src/
            ├── run_for_all_the_projects.py <--- here
            ├── requirements.txt 
            └── README.md
- **merge_excels.py**

        - Used to merge excels of multiple projects based of the outcome of run_for_all_the_projects.
        - Move the script to the root folder of the project
            Refactoring-recognition-for-python
            ├── Results/
            ├── Documentation/
            ├── src/
            ├── merge_excels.py <--- here
            ├── requirements.txt 
            └── README.md
        - the input for this script is the Results folder inside the project folder
