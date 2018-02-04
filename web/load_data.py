from . import db
from .models import Project



projects = [
    [1,'CS Website',
        'Not only will this new website show off each of our projects, tasks and quick links to all of our resources and tools the club is using, but it will also become a hub for our new and current members to digest a project and become a great help! Any new top news, upcoming event, and project updates will be posted to our site for everyone to view. My vision in this website is for everyone, members, programmers, and potental members to stay informed about progress and details in every project. Members and potental members can comment and give feedback to any project as a comment feed in each project. Each project contains a detailed description about goals, requirments, and the platform as well as images, list of participating members, and a timeline of events and achivements. As for members, a club member can create a profile and fill in a picture, short and long bios, and show off any work done outside of the club. Quick links will show all of the projects, listed on the website, each member has participated in. As for the About and Contact Us pages, egeryone will have the opprotunuty to ask how to join the club and learn about what we do.',
        'A new website to showoff what we do as a club',
        'In Progress',
        'Finalizing the Resources Tab',
        {},
        {
            "checkvist":'https://checkvist.com/checklists/563656-csc-cs-website',
            "figma": 'https://www.figma.com/files/project/64393/Club-Website',
            "waffle": 'https://waffle.io/SRJC-Computer-Science-Club/cs-website',
            "github": 'https://github.com/SRJC-Computer-Science-Club/cs-website'
        },
        []
    ],
    [14,'Firefighter',
        '',
        '',
        'On Hold',
        'Designing Plans',
        {},
        {},
        [
        ]
    ],
    [12,'Jumpnotes',
        'JumpNotes is a Simple, Quick, Easy to use, Note taking app that "auto-magically" backups everything to a server. Using the hottest new technology we built JumpNotes using React Native for the app frontend, Node.js for the backend server magic, and used Mongodb to implement our database.',
        'Simple, Quick, Easy to use, Note taking app',
        'In Progress',
        'Delegating Tasks',
        {},
        {},
        [
        ]
    ],
    [13,'Book Stack',
        '',
        '',
        'In Progress',
        'Creating Outline',
        {},
        {},
        [
        ]
    ],
    [5,'Line Follower',
        '',
        '',
        'In Progress',
        'Crunch Time!',
        {},
        {
            "robogames": 'http://robogames.net/rules/line-following.php',
            "checkvist": 'https://checkvist.com/checklists/581272-csc-line-follower',
            "waffle": 'https://waffle.io/SRJC-Computer-Science-Club/line-follower',
            "github": 'https://github.com/SRJC-Computer-Science-Club/line-follower'
        },
        []
    ],
    [11,'Space Junkies',
        'I am heading the design and production of Space Junkies with a wonderful team! The game is still in its youth, but we are getting a lot done. We hope to share more information about this game in the following months.',
        'I am heading the design and production for Space Junkies with a wonderful team!',
        'In Progress',
        '',
        {},
        {
            "github": 'https://github.com/SRJC-Computer-Science-Club/Ludum-Dare-38-Space-Junkies',
            "waffle": 'https://waffle.io/SRJC-Computer-Science-Club/Ludum-Dare-38-Space-Junkies',
            "drive": 'https://drive.google.com/drive/folders/0B3wyRcLxpH4jXzRDMHdROW9ENTg?usp=sharing',
            "checkvist": 'https://checkvist.com/checklists/614869-csc-space-junkies'
        },
        [
        ]
    ],
    [0,'Micromouse',
        '',
        'An autonomous maze solving robot mouse',
        'Archived',
        '',
        {},
        {
            "checkvist": 'https://checkvist.com/checklists/542765',
            "waffle": 'https://waffle.io/SRJC-Computer-Science-Club/micromouse',
            "github": 'https://github.com/SRJC-Computer-Science-Club/micromouse'
        },
        []
    ],
    [9,'Club App',
        'GitHub issues are great for saving todos and progress needed to be made that is related to code. But, what about general tasks that do not relate to any repository on GitHub? Well, that\'s where our app comes in. We\'re adding as many features as we can from GitHub into a single app that also contains a shared task manager.',
        'A central hub for the club to use to view and edit GitHub issues, comments and pull requests as well as a task manager replica of Trello.',
        'On-Hold',
        'Building navigation',
        {},
        {
            "invision": 'https://invis.io/K8AX0FZBN',
            "figma": 'https://www.figma.com/files/project/161855/Club-App',
            "github:": 'https://github.com/SRJC-Computer-Science-Club/cs-app-react-native'
        },
        []
    ],
    [7,'SRJC Scheduler',
        'Quickly load classes onto a friendly calendar all at once! If instructors isn\'t your main concern, nicely look at all available times for a course. The SRJC Scheduler is founded and created by <a href="/members/0">Ben Hough</a>',
        'Schedule your next semester with SRJC Scheduler!',
        'Rebuilding',
        'Mockups looking good',
        {},
        {
            "scheduler": 'http://srjcscheduler.com/',
            "github": 'https://github.com/SRJC-Computer-Science-Club/srjc-scheduler'
        },
        []
    ],
    [3,'Function Fighters',
        'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'An AI battle arena simulator',
        'Archived',
        'Would you like to join?!',
        {},
        {
            "github": 'https://github.com/joshuasrjc/function-fighters'
        },
        []
    ],
    [10,'ShortLink',
        "<a href='/members/12'>Kyle</a> joined <a href='/events/0'>Make-a-thon</a> to make his first iOS app. It was a success!<br><br>ShortLink brings link shortening to iOS, once more, using Google's public API to enter any valid url and gives back a working shorten link! This app is used as an introductory to iOS Development.",
        "The first iOS application to make it to the club",
        "Archived",
        "Have a Mac? Join the iOS Team",
        {},
        {
            "github": 'https://github.com/Kyle1668/Short-Link'
        },
        []
    ],
    [8,'Dreamscape',
        '',
        '',
        'Resigned',
        '',
        {},
        {
            "drive": 'https://drive.google.com/drive/folders/0B23hDSQTMIITY2hVZ3dzd3NuQm8?usp=sharing'
        },
        [
        ]
    ],
    [6,'Retailer',
        'Created with <a href="https://unity3d.com" target="_blank">Unity 3D</a>, Retailer is an all-out, in-depth simulation of a store manager. You, the store manager, will control and oversee many things such as who you hire, promote, penaltize and transfer in your store. Chose which vendors you\'d like to partner with as well as what merchandise you\'ll want to sell. Will your store be a grocery store, hardware store or an outlet? Every small detail will be made by you, the store manager.',
        'Retail simulation of everything that has to do with retail.',
        'Resigned',
        '',
        {},
        {
            "checkvist": 'https://checkvist.com/checklists/587081-csc-retail',
            "waffle": 'https://waffle.io/SRJC-Computer-Science-Club/Retailer',
            "github": 'https://github.com/SRJC-Computer-Science-Club/retailer'
        },
        [
            'preview of ui-1.png',
            'preview-1.jpg',
            '3d model-1.png'
        ]
    ],
    [4,'Quad-Copter',
        "<a href=/members/3'>I</a> worked on a landmine detection quadcopter with college <a href='/members/9'>Yekalo Aberha</a>. Mr. Aberha and I, coded and build a lidar two diminsional mapping sensor. To create a graph of points to repersent what the sensor is resiving which was edges of objects.<br /><br />x = r × cos( θ )y = r × sin( θ )<br /><br />We found out that the sensor was not working because we needen to conver the rotation of the sensor, into (x,y) coordiates.",
        '',
        'Archived',
        '',
        {},
        {},
        []
    ],
    [2,'2D Platformer',
        'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'A simple 2d platformer game',
        'Resigned',
        '',
        {},
        {
            "checkvist": 'https://checkvist.com/checklists/560653',
            "waffle": 'https://waffle.io/SRJC-Computer-Science-Club/2d-platformer',
            "github": 'https://github.com/SRJC-Computer-Science-Club/2d-platformer'
        },
        [
            'main-character-1.png',
            'main-character-2.png',
            'main-character-3.png',
            'main-character-sprite-1.png'
        ]
    ]
]

for project in projects:
    db_project = Project(title=project[1], description=project[2], description_short=project[3], status=project[4], post=project[5])
    db.session.add(db_project)

db.session.commit()
