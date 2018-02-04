from . import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    description = db.Column(db.Text)
    description_short = db.Column(db.String(256))
    status = db.Column(db.String(32))
    post = db.Column(db.String(128))
    members = []
    images = []
    # links = db.Column(db.Integer, db.ForeignKey("link"))


# class Milestone(db.Model):
#
#
# function Project( id, title, description, description_short, status, post, milestones, links, images )
# {
#     this.id = id;
#     this.title = title;
#     this.description = description;
#     this.description_short = description_short;
#     this.status = status;
#     this.post = post;
#     this.milestones = milestones;
#     this.links = links;
#     this.images = images;
# }
# 	new Project(
# ID:                   1,
# title:                'CS Website',
# description:		    'Not only will this new website show off each of our projects, tasks and quick links to all of our resources and tools the club is using, but it will also become a hub for our new and current members to digest a project and become a great help! Any new top news, upcoming event, and project updates will be posted to our site for everyone to view. My vision in this website is for everyone, members, programmers, and potental members to stay informed about progress and details in every project. Members and potental members can comment and give feedback to any project as a comment feed in each project. Each project contains a detailed description about goals, requirments, and the platform as well as images, list of participating members, and a timeline of events and achivements. As for members, a club member can create a profile and fill in a picture, short and long bios, and show off any work done outside of the club. Quick links will show all of the projects, listed on the website, each member has participated in. As for the About and Contact Us pages, egeryone will have the opprotunuty to ask how to join the club and learn about what we do.',
# description_short:    'A new website to showoff what we do as a club',
# status:		        'In Progress',
# post:		            'Finalizing the Resources Tab',
# milestones:	        {},
# links:		        {
# 	    		            checkvist: 'https://checkvist.com/checklists/563656-csc-cs-website',
# 		    	            figma: 'https://www.figma.com/files/project/64393/Club-Website',
# 	    		            waffle: 'https://waffle.io/SRJC-Computer-Science-Club/cs-website',
# 		    	            github: 'https://github.com/SRJC-Computer-Science-Club/cs-website'
# 	        	        },
# images	            []
# ),