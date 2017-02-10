# PRODUCT/TEAM NAME

---------------

## Iteration 1

>Start date (Planning): Monday, February 6 2017

>End date (Review): Thursday, February 9 2017

## Process

Our development process can be described as a loose version of Scrum. We will adhere to practices outlined by Scrum, but are changing certain facets to better fit a remote team. The length of each sprint will be two weeks long due to the timing of team deliverables in the course fitting multiples of two weeks.


#### Roles and Responsibilities

###### Main Roles

*Main roles are meant to give a clear and defined role to every member in the team. They are not the only roles that one would have.*

| Role | Responsibility | Member |
| --- | --- | --- |
| Front-end Master | Primarily works with the front-end (design, scripting) and is responsible for maintaining development branches associated with the front-end, including creating the sprint backlog and merging related PRs | Ian |
| Back-end Master | Primarily works with the back-end (user profiling, routing, security, database management, middleware...) and is responsible for maintaining development branches associated with the back-end, including creating the sprint backlog and merging PRs | Sakshaat |
| Chief Data Analyst | Primarily works with the data analysis (parameterization, historical analysis, suggestion algorithms) and is responsible for maintaining development branches associated with the data analysis section, including creating the sprint backlog and merging PRs | Aaron |
| Technical Lead | Works with the entire stack, merging any outstanding PRs, helping to create high-level algorithms and keeping code standards and RESTful endpoints consistent | Akshay |
| Business/QA Lead | Helps to coordinate the team for sync meetings, ensures presentation quality of the product and of deliverables, and helps to create high-level algorithms through researching resources and APIs | Harold |

###### Secondary Roles

*Secondary roles are not completely rigid as we allow any member to contribute to any part of the project.*

| Role | Responsibilities | Members |
| --- | --- | --- |
| Front-end Developer | Contribute to the front-end development, creating PRs for the Front-end Master | Sakshaat, Harold |
| Back-end Developer | Contribute to the back-end development, creating PRs for the Back-end Master | Ian, Aaron, Harold |
| Data Analyst | Contribute to the data analysis section, creating PRs for the Chief Data Analyst | Sakshaat, Harold |
| QA Engineer | Document code and test major features in preparation for sprint demonstrations | Everyone |

###### Other Roles

| Role | Responsibilities | Members |
| --- | --- | --- |
| Scrum Master | Conduct retrospective meetings at the end of sprints and improve the workflow and role management of the project throughout each weekly sync meeting | Akshay |
| Product Owner | Maintain a consistent vision and create the product backlog | Aaron, Harold |
| General Member | Work on creating deliverable documents, attend all review and planning meetings, and check Slack on a constant basis | Everyone |


#### Events

Development will mostly be happening remotely, as many of the team members are either working full-time or are unable to coordinate schedules to meet in-person for development purposes. Due to this, the team will continue to meet online over Discord as well as every Monday night in-person for weekly planning and review meetings, as well as ad-hoc standup meetings in which we will conduct weekly sync sessions. There will be a minimum of one meeting per week.

We will also consider scheduling ad-hoc code review sessions on weekends in which only certain group members would be required to attend.

Review meetings and retrospective meetings will be merged. During review meetings, we will review current progress, make any changes to our current development process if necessary and plan the next steps (whether this entails planning the next sprint, or the next development steps).

#### Artifacts

We plan to create documents which will be pushed to the GitHub repository, including product backlogs and sprint backlogs. In addition, we will use **[ZenHub](https://www.zenhub.com/)**, a browser extension that changes GitHub issues into task board formats, and we will use these as our task board artifacts. We would also keep track of what tasks need to be done by scheduling them as "To-do" issues on GitHub, and we will create to-do lists from these to serve as artifacts.

A sample ZenHub board can be seen below:

![ZenHub sample board](https://images.g2crowd.com/uploads/attachment/file/55157/expirable-direct-uploads_2Fa01fc47b-4174-4ddf-bf1a-98d02183b874_2Fzenhubboard.png)

Tasks will be assigned to teammates on GitHub through the web interface. This would be done depending on what the project requires at any given time. As each team member as a clear, defined main role, issues would first be assigned to the one(s) in charge of the respective part of the project. Then, the issue can be delegated to any relevant team members (i.e. those who are developers as a secondary role) for greater efficiency if necessary.

We can also prioritize tasks by labelling them as "High-priority". This would be done whenever an issue blocks some other part of the project from being developed, and/or when an issue impedes the progress of the sprint. The development team is expected to solve these issues first before any others. If there are multiple issues that are high-priority, the development team will work on them in a logical order that reflects the overall significance of the issue to the project.

Finally, we will also create data visualization artifacts such as burndown graphs by making use of ZenHub's analysis tools. We will be analysing these in our sprint retrospective meetings in order to comment on our development process.

A sample data visualization artifact can be seen below. This is an interactive burndown graph.

![Chart](https://cristinasantamarina.files.wordpress.com/2015/06/zenhub-burndown-chart.png)

#### Workflow

On GitHub, we plan to use forks and feature branches to maintain our development.

The `master` branch in the `csc301-winter-2017` version of the repository will serve as our base reference and submission branch. Changes meant for production will be pushed to this branch on a regular basis. We will push this branch to our production hosting environments manually whenever appropriate for presentation.

We will also maintain a `develop` branch on an ongoing basis on the `csc301-winter-2017` version of the repository. It will serve as reference for us, and will be the central repository to which pull requests from respective forks are accepted to. At the end of each sprint, if the `develop` branch is fully tested and ready for production, we will issue a pull request to `master` which will be merged.

After the `develop` branch, we will maintain individual forks. The reasoning for using forking (as opposed to branching further) is that we do not have administrative access to the central repository. By forking, we are able to use our respective forks with Continuous Integration and/or with automated hosting services.

Individual `develop` branches will be used for our development hosting environments. Each individual will also create `feature` branches on an ongoing basis, which will be merged back to `develop`, which will then be used to create a pull request to our central repository's `develop` branch.

An explanation of this workflow can be found at the [Atlassian Gitflow Workflow page](https://www.atlassian.com/git/tutorials/comparing-workflows#gitflow-workflow) or the [GitHub workflow page](https://guides.github.com/introduction/flow/).


## Product

#### Goals and tasks

 Our goals for this iteration is define a clear vision for our product, this includes the core features and the overall user experience. Defining our product and core feature early on will allow us to have a better understanding of what technology we need to achieve our vision.

1. Define core features for our product. This should essentially be what an Minimum Viable Prototype would have. We will likely draw out our application's basic flow with a sketch and decide our key user stories and/or core features from there.

2. Delegate clear and meaningful roles for each member of the team. Each member of the team should know what they are responsible for, and should be willing to do it. We will likely have a planning session where we are able to decide these roles.

3. Create user personas for our application. This will allow us to tailor our application's user interface and overall look and feel to our user base. This will allow us to get started on the high-level interface sketches and basic prototyping. We will likely be using a tool such as Xtensio for this.

4. Research algorithms, tools and datasets for the core of our data analysis. If there are any libraries that simplify our task, we should find them right away to minimize our development costs. We should look into whether analyzing the crypto-currency market has been attempted by any other open source projects or public blogs or articles as well. Seeing as this will get the data analysis component of our application started, this should be a priority. We will likely use search engines to gather info and compile it into a central document. 

5. Decide on a tech stack to use. We should consider the pros and cons of various languages and frameworks while also weighing in on which team members are proficient in each of these languages and frameworks, respectively. Deciding on a tech stack as soon as possible will allow us to start development sooner. We will look at similar projects and see what technologies were used in those projects, and we will have a review meeting where we will survey each group member as to his proficiencies.

#### Artifacts

 * Rough sketch - a high level overview of the flow for our product. This sketch should only describe "what" the application does. This sketch will allow us to determine the core features we need to implement.
 
 * Xtensio - an easy to use platform to create, collaborate, share and present user personas.