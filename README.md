# Refactor pattern recognition for Python
### Implemented Refactors

| Category                        | Refactor                                   | Color                                           | File Location                                      | Documentation                                       |
|---------------------------------|--------------------------------------------|-------------------------------------------------|----------------------------------------------------|-----------------------------------------------------|
| Moving Features between Objects |                                             |                                                 |                                                    |                                                     |
|                                 | Move Method                                | ![](https://placehold.co/10x10/000066/000066.png) | [MoveMethod.py](src/Refactors/MovingFeaturesBetweenObjects/MoveMethod.py)       | [MoveMethod.md](Documentation/MovingFeaturesBetweenObjects/MoveMethod.md)           |
|                                 | Extract Class                              | ![](https://placehold.co/10x10/00408c/00408c.png) | [ExtractClass.py](src/Refactors/MovingFeaturesBetweenObjects/ExtractClass.py)   | [ExtractClass.md](Documentation/MovingFeaturesBetweenObjects/ExtractClass.md)       |
|                                 | Inline Class                               | ![](https://placehold.co/10x10/0095bf/0095bf.png) | [InlineClass.py](src/Refactors/MovingFeaturesBetweenObjects/InlineClass.py)     | [InlineClass.md](Documentation/MovingFeaturesBetweenObjects/InlineClass.md)         |
|                                 | Move Field                                 | ![](https://placehold.co/10x10/00ffff/00ffff.png) | [MoveField.py](src/Refactors/MovingFeaturesBetweenObjects/MoveField.py)         | [MoveField.md](Documentation/MovingFeaturesBetweenObjects/MoveField.md)             |
| Organizing Data                 |                                             |                                                 |                                                    |                                                     |
|                                 | Replace Array with Object                 | ![](https://placehold.co/10x10/993366/993366.png) | [ReplaceArrayWithObject.py](src/Refactors/OrganizingData/ReplaceArrayWithObject.py) | [ReplaceArrayWithObject.md](Documentation/OrganizingData/ReplaceArrayWithObject.md) |
|                                 | Replace Magic Number with Symbolic Constant | ![](https://placehold.co/10x10/ff33ff/ff33ff.png) | [ReplaceMagicNumberWithSymbolicConstant.py](src/Refactors/OrganizingData/ReplaceMagicNumberWithSymbolicConstant.py) | [ReplaceMagicNumberWithSymbolicConstant.md](Documentation/OrganizingData/ReplaceMagicNumberWithSymbolicConstant.md) |
|                                 | Encapsulate Collection                     | ![](https://placehold.co/10x10/ff6600/ff6600.png) | [EncapsulatedCollection.py](src/Refactors/OrganizingData/EncapsulatedCollection.py) | [EncapsulatedCollection.md](Documentation/OrganizingData/EncapsulatedCollection.md) |
|                                 | Encapsulate Field                          | ![](https://placehold.co/10x10/ff6699/ff6699.png) | [EncapsulatedField.py](src/Refactors/OrganizingData/EncapsulatedField.py) | [EncapsulatedField.md](Documentation/OrganizingData/EncapsulatedField.md) |
| Simplifying Method Calls         |                                             |                                                 |                                                    |                                                     |
|                                 | Rename Method                              | ![](https://placehold.co/5x5/003300/003300.png) | [RenameVariable.py](src/Refactors/SimplifyingMethodCalls/RenameVariable.py) | [RenameVariable.md](Documentation/SimplifyingMethodCalls/RenameVariable.md) |
|                                 | Add Parameter                              | ![](https://placehold.co/10x10/005522/005522.png) | [AddRemoveParameter.py](src/Refactors/SimplifyingMethodCalls/AddRemoveParameter.py) | [AddRemoveParameter.md](Documentation/SimplifyingMethodCalls/AddRemoveParameter.md) |
|                                 | Remove Parameter                           | ![](https://placehold.co/10x10/007744/007744.png) | [AddRemoveParameter.py](src/Refactors/SimplifyingMethodCalls/AddRemoveParameter.py) | [AddRemoveParameter.md](Documentation/SimplifyingMethodCalls/AddRemoveParameter.md) |
|                                 | Preserve Whole Object                      | ![](https://placehold.co/10x10/009966/009966.png) | [PreserveWholeObject.py](src/Refactors/SimplifyingMethodCalls/PreserveWholeObject.py) | [PreserveWholeObject.md](Documentation/SimplifyingMethodCalls/PreserveWholeObject.md) |
|                                 | Introduce Parameter Object                | ![](https://placehold.co/10x10/ffff00/ffff00.png) | [IntroduceParameterObject.py](src/Refactors/SimplifyingMethodCalls/IntroduceParameterObject.py) | [IntroduceParameterObject.md](Documentation/SimplifyingMethodCalls/IntroduceParameterObject.md) |
|                                 | Remove Setting Method                      | ![](https://placehold.co/10x10/ffff55/ffff55.png) | [RemoveSettingMethod.py](src/Refactors/SimplifyingMethodCalls/RemoveSettingMethod.py) | [RemoveSettingMethod.md](Documentation/SimplifyingMethodCalls/RemoveSettingMethod.md) |
|                                 | Hide Method                                | ![](https://placehold.co/10x10/ffffbf/ffffbf.png) | [HideMethod.py](Documentation/SimplifyingMethodCalls/HideMethod.py)       | [HideMethod.md](src/Refactors/SimplifyingMethodCalls/HideMethod.py)           |
|                                 | Replace Error Code with Exception          | ![](https://placehold.co/10x10/ff0000/ff0000.png) | [ReplaceErrorCodeWithException.py](src/Refactors/SimplifyingMethodCalls/ReplaceErrorCodeWithException.py) | [ReplaceErrorCodeWithException.md](Documentation/SimplifyingMethodCalls/ReplaceErrorCodeWithException.md) |
|                                 | Replace Exception with Test                | ![](https://placehold.co/10x10/ff3300/ff3300.png) | [ReplaceExceptionWithTest.py](src/Refactors/SimplifyingMethodCalls/ReplaceExceptionWithTest.py) | [ReplaceExceptionWithTest.md](Documentation/SimplifyingMethodCalls/ReplaceExceptionWithTest.md) |
| Dealing with Generalization       |                                             |                                                 |                                                    |                                                     |
|                                 | Pull Up Field                | ![](https://placehold.co/10x10/79443b/79443b.png) | [PullUpField.py](src/Refactors/DealingWithGeneralizations/PullUpField.py) | [PullUpField.md](Documentation/DealingWithGeneralizations/PullUpField.md) |
|                                 | Push Down Field                | ![](https://placehold.co/10x10/e3dac9/e3dac9.png) | [PushDownField.py](src/Refactors/DealingWithGeneralizations/PushDownField.py) | [PushDownField.md](Documentation/DealingWithGeneralizations/PushDownField.md) |
|                                 |  Pull Up Method               | ![](https://placehold.co/10x10/ffccff/ffccff.png) | [PullUpMethod.py](src/Refactors/DealingWithGeneralizations/PullUpMethod.py) | [PullUpMethod.md](Documentation/DealingWithGeneralizations/PullUpMethod.md) |
|                                 |  Push Down Method               | ![](https://placehold.co/10x10/9900ff/9900ff.png) | [PullUpMethod.py](src/Refactors/DealingWithGeneralizations/PushDownMethod.py) | [PushDownMethod.md](Documentation/DealingWithGeneralizations/PushDownMethod.md) |
|                                 |  Pull Up Constructor Body                  | ![](https://placehold.co/10x10/993333/993333.png) | [PullUpConstructorBody.py](src/Refactors/DealingWithGeneralizations/PullUpConstructorBody.py) | [PullUpConstructorBody.md](Documentation/DealingWithGeneralizations/PullUpConstructorBody.md) |
|                                 |  Extract Subclass                  | ![](https://placehold.co/10x10/99cccc/99cccc.png) | [ExtractSubclass.py](src/Refactors/DealingWithGeneralizations/ExtractSubclass.py) | [Extract Subclass](Documentation/DealingWithGeneralizations/ExtractSubclass.md) |
|                                 |  Extract Superclass                  | ![](https://placehold.co/10x10/99ff00/99ff00.png) | [ExtractSuperclass.py](src/Refactors/DealingWithGeneralizations/ExtractSuperclass.py) | [Extract Superclass](Documentation/DealingWithGeneralizations/ExtractSuperclass.md)
|                                 |  Collapse Hierarchy                 | ![](https://placehold.co/10x10/99ffff/99ffff.png) | [CollapseHierarchy.py](src/Refactors/DealingWithGeneralizations/CollapseHierarchy.py) | [Collapse Hierarchy](Documentation/DealingWithGeneralizations/CollapseHierarchy.md)

### Project Structure
```bash
Refactoring-recognition-for-python
├── Results/
├── Documentation/
│   ├── DealingWithGeneralizations/
│   │   ├── PullUpConstructorBody.md
│   │   └── ...
│   ├── MovingFeaturesBetweenObjects/
│   │   ├── ExtractClass.md
│   │   └── ...
│   ├── OrganizingData/
│   │   ├── EncapsulatedCollection.md
│   │   └── ...
│   └── SimplifyingMethodCalls/
│       ├── AddRemoveParameter.md
│       └── ...
├── src/
│   ├── Refactors/
│   │   ├── DealingWithGeneralizations/
│   │   │   ├── PullUpConstructorBody.py
│   │   │   └── ...
│   │   ├── MovingFeaturesBetweenObjects/
│   │   │   ├── ExtractClass.py
│   │   │   └── ...
│   │   ├── OrganizingData/
│   │   │   ├── EncapsulatedCollection.py
│   │   │   └── ...
│   │   └── SimplifyingMethodCalls/
│   │       ├── AddRemoveParameter.py
│   │       └── ...
│   ├── util/
│   │   ├── Line_utilities.py
│   │   └── ...
│   ├── DiffBlock.py
│   ├── File.py
│   ├── Line.py
│   ├── Regactor.py
│   ├── config.py <-- Create this file with the content that is described in the next section
│   └── main.py
├── requirements.txt 
└── README.md
```


### Install requirements
Python version : **3.9.2**

Required imports:
#### Used in the core program
- **beautifulsoup4**

    (to read the html files that difflib library returns)
- **thefuzz**

    (to compare strings)
- **minify_html**

    (to reduce the size of the html files)
- **XlsxWriter** and **pandas**

    (to read and write excel files for the results)
#### Used in the extra scripts files
- **Requests** 

    (to download projects from github,used in the extra scripts file download_releases_from_github.py)
- **progress** and **tabulate**
    
    (to generate a progress bar and table,used in the extra scripts file get_how_may_are_done.py)



```sh
 pip install -r requirements.txt
```
## Create config.py
Inside the **src** folder create a config.py file with the following content:
```python
#used by download_releases_from_github.py
GITHUB_TOKEN = 'TOKEN'
# generate a token here https://github.com/settings/tokens 
# check the permissions for :
#  - 'Read access of projects' 
#  - 'Download packages from GitHub Package Registry'
MAX_RELEASES_TO_DOWNLOAD = 30 #maximum number of releases to download

#used by get_how_may_are_done.py and run_for_all_the_projects.py
PROJECT_FOLDER_PATH= r"path_to_projects_folder" #path to the project folder

#used by html_per_refactor.py from main program
MINIFY_HTML_BOOL = True #use the minify html library to reduce the size of the html files
``` 
### How to use
#### Use case 1 - compare two versions:
```sh
python src/main.py version_1_path version_2_path
```
#### Use case 2 - compare project folder :
```sh
python src/main.py project_name_path
```
#### The project_name_path is the path to the project folder that contains folders with different versions
#### project_name_path folder structure example :
 ```bash 
 Project name 
├── version_1
├── version_2
└── ...
 ```


### Results
Creates a folder containing the results.
#### The output for comparing two versions only
```bash
Results 
└── [version_1]&[version_2]
    ├── html_files/
    ├── Execution.txt
    ├── Refactors.xlsx
    └── Refactors_Tree.html
```
#### The output for comparing project folder
```bash
Results 
└── project_name
    ├── html_files/
    ├── Execution.txt
    ├── [project_name]Refactors.xlsx
    └── [project_name]Refactors_Tree.html
```
### Extra scripts
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
