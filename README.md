# SOLVE-IT



## Branching Convention
We follow a branching convention to manage our codebase effectively. The convention is as follows:

- `main`: The main branch that represents the production-ready code.
- `dev`: The development branch where new features are integrated and tested.
- `feature/your-feature`: Branches  for developing new features. ex: `feature/leaderboard-points`
- `bugfix/your-bugfix`: Branches  for fixing bugs. ex: `bugfix/upload-file`
- `conf/your-conf`: Branches  for conficurations . `conf/django-chanels`

<!-- - `hotfix/your-hotfix`: Branches created for critical bug fixes in the production code. These branches are created from the `main` branch and merged back into it once the hotfix is complete. -->

When creating a new branch, make sure to give it a descriptive name that reflects the purpose of the branch. For example, if you are working on a feature to add user authentication, you can create a branch named `feature/user-authentication`.

It is important to follow this branching convention to ensure a smooth and organized development process. By using separate branches for different features and bug fixes, we can easily track changes, collaborate effectively, and maintain a stable codebase.

<!-- ## Description
SOLVE-IT is a project aimed at solving complex problems using innovative solutions. This repository contains the source code and documentation for the project.

## Features
- Feature 1: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
- Feature 2: Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
- Feature 3: Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.
-->
## Installation
1. Clone the repository: 
    ```bash
    git clone https://github.com/TechGeeks-Club/Solve-it.git
    ```

2. Install the dependencies: 
    ```bash 
    pip install -r reuirements.txt
    ```
3. run the server: 
    ```bash 
    uvicorn src.asgi:application  --host 0.0.0.0 --port 8000 #use --reload for developement
    ```

<!-- ## Usage
1. Run the application: `npm start`
2. Open your browser and navigate to `http://localhost:3000` -->
<!-- 
## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:
1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request -->

<!-- ## License
This project is licensed under the [MIT License](LICENSE). -->

<!-- ## Contact
For any inquiries or feedback, please contact us at solve-it@example.com. --> 
