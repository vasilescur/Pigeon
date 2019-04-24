<p align="center">
  <img src="https://user-images.githubusercontent.com/10100323/54144603-6f555f00-4402-11e9-9422-13f36e4f6cf8.png">
</p>

<p align="center">
  A hyper-local, real-time, collaborative platform for citizen journalism.
</p>

<br/><br/>

# The Prototype

## Usage

### Requirements:

- Python 3
- Django

Clone repo. Run:

```bash
python manage.py runserver
```

Browse to `localhost:8000`.

### License

As of now, this project is available under the MIT License. See `LICENSE` file for details.


# Motivation, Background, and Written Report

### Introduction

In today’s age of mass digitization and urbanization, local journalism is being steadily taken over by big city media outlets, taking the focus away from local, immediately relevant news. Efforts such as Patch and WikiNews have tried to address this issue in various ways, with varying levels of success. After examining the issues at hand, and why addressing them is important to the community and news audience, I will present a prototype of a new platform that aims to address these problems in an innovative new way—through collaborative, hyperlocal citizen journalism.

### The Problem: Background and Relevance

As more and more people turn away from newspapers and magazines and towards websites and social media to get the daily scoop, the focus of news has changed from local events reporting to consistent state, national, and international news. Most news that people consume comes from a relatively small distribution of sources, often concentrated in the big cities in close proximity to the audience members. This makes it harder for people to find news that is directly relevant to them and to their community, because the big news organizations don’t have enough reporting manpower to cover all of the small communities around the city, and the local outlets are seeing decreased revenue due to intense competition with the big organizations. In addition, this decreased amount of news outlets reporting on each story leads to a lower level of credibility, because fact-checking the claims and details in the articles that are published cannot be corroborated against as many other sources.

### The Solution: Hyper-Local Citizen Journalism

I believe that a strong solution to this problem is the introduction of a comprehensive, collaborative hyper-local citizen journalism platform. Citizen journalism has been seriously analyzed and studied in the past, and has been proven to work successfully in some scenarios. For example, in a 2007 Guardian article, Rory O’Connor explains the vast success of the popular Korean news platform OhMyNews—with a motto of “Every citizen is a reporter,” this citizen journalism platform has “revolutionized the media environment in South Korea” (O’Connor), proving that citizen journalism can be practical and effective at scale. 

A hyper-local news reporting platform can help to bring focus back from centralized large media organizations into the local communities in which local reporting is so vital. However, some may argue that “many hyper-local or niche journalism initiatives have not been sustainable” (Wall, “Citizen Journalism”). But others, such as Jeff Bercovici, explain why—“ it was the decision to ramp up the size of the operation so rapidly” (“The Fatal Error”). As we’ll see later (“Business and Strategy Considerations”), my platform will attempt to avoid this issue by carefully and methodically sticking to a well-defined model for determining where to expand.

### Competitors and Other Similar Platforms

There have been a few different attempts to launch similar news platforms, from various companies such as Patch and the Wikimedia Foundation. Patch is a news platform that offers sub-websites for hyperlocal news, in which articles are contributed mostly by Patch employees, but also by certain citizens. This was a good idea, and the way that Patch executed it, in my opinion, was very well done for the scope of the project. The site works decently and has a considerable amount of traffic. However, I believe that it is missing one important feature: There is no capability for users to submit edits and improvements to others’ articles or posts. This means that a team of editors is required to spend time manually proofreading, editing, and improving each article before it can be published, and inaccuracies can be easily overlooked due to the small number of people reviewing each article before it is made public. This can easily lead to the spread of false or incomplete information that slips through the cracks of the editing process. The audience/community is essentially powerless to correct such issues without contacting Patch directly—a system that certainly would not scale well to thousands of community websites. In addition, allowing users to contribute more intensely to content creation via editing and collaborative writing would free up the company’s resources, perhaps allowing it to have succeeded in its ambitiously rapid expansion.

The Wikimedia Foundation (the group behind Wikipedia and other similar products) has created a platform known as WikiNews that tries to alleviate this issue by allowing readers to edit articles just as they would edit a page on Wikipedia. On WikiNews, while most articles are indeed proposed and written by citizens/readers, this process does not occur in real time: users have to wait for the first author to finish a draft of the article before they can begin editing and suggesting changes. As these changes may be happening at the same time,  such a system may give rise to merge conflicts and redundancy. In addition, WikiNews, while weakly organized by location, is more focused on large-scale and international news, and therefore does not really fit into the hyperlocal category. Many medium-sized cities appear as categories there, but Durham, for example, does not. 

### Overview of Platform

My prototype news platform provides all of the hyperlocal organization structure of Patch sites, together with the crowd-sourced philosophy of WikiNews. In addition, future iterations will feature a Google Docs style editor allowing for instant, real-time collaboration when drafting and editing an article. Instead of each author writing a headline and a first draft, and only then submitting the article for review, the workflow is organized as follows:

<img width="1245" alt="Screen Shot 2019-04-23 at 10 35 50 PM" src="https://user-images.githubusercontent.com/10100323/56628535-2f47e580-6618-11e9-8613-27fe38ebf7bd.png">

As current events take place in the community, anyone can contribute potential headlines to the article queue, which is periodically reviewed and organized by the small editor team assigned to that location. This queue is worked on by citizens, journalists, and eventually company employees. Using a Google Docs style editor, they can collaborate on articles in real time by adding sources, information, and checking each other’s work. When the article is considered to be pretty much finished, it is sent to the Editing Workspace, where particularly experienced citizens, along with journalists and members of the company’s team, proofread and approve the articles. At the same time, automated and manual fact-checking processes work to verify the integrity of the claims made in the article, to prevent intentional or accidental misinformation. When the article is approved, a live-updating version is posted to the local site, and may be sent to be embedded in the webpages of other nearby news outlets. As eventual other changes and edits are made to the article, these changes are reflected in real time in the embedded versions in the pages where the article is published.

### The Prototype

After solidifying the general outline of the workflow and planning how this platform would work, I implemented a proof-of-concept prototype web application. I used the Django Python backend web framework, in combination with a HTML/CSS/JavaScript frontend, to create a functioning prototype of the platform, including a main page, account creation and login, adding headlines to the queue, an administrative dashboard for approving and publishing stories, and a robust, rich text editor for article content. The source code of my prototype is available in this GitHub repository.

### Business and Strategy Considerations

Although my initial idea for this platform included the capability for any user to (after confirming that it doesn’t already exist) create a community page for their town, more extensive research into the history of Patch and its shortcomings reveals that perhaps a more conservative strategy would be beneficial. In a New York Times column, David Carr explains how Patch’s deviation from its original strategy—only expanding to locations that it predicted would be successful—lead to its effective demise. Therefore, for my platform, a key component of the expansion strategy would include implementing an audience-prediction algorithm similar to the one used by Patch to determine how successful a certain new community page might be, and erring on the conservative side regarding new expansions and growth. 

### Future Development and Plans

The platform that I have laid out has some possible flaws. One important issue is spam—how can we regulate the content posted to make sure that it is all genuine, relevant, and not bot-generated garbage? Along the same lines, how can we avoid the problem of so-called “Fake News”—misinformation or incomplete information that slips through the proofreading process? A possible solution to these quality-control issues could be the implementation of existing automated fact-checking services, or a system of verification in which established experienced users of the site have more power in determining whether other article drafts are of good enough quality to be submitted for the final editing and publication workspace. Other problems, such as potential political bias, could arise when citizens untrained in objective reporting begin writing politically-oriented articles. However, this problem should ideally balance itself out, as the wide variety of people helping to draft each article, and those submitting edits afterwards, will likely hold diverse political beliefs and tend to objectively fact-check opposing statements.

With the advent of digital news platforms and online publications as the primary source of news for most Americans today, we need an innovative way to cope with the overpowering concentration of reporting towards big city news organizations. Patch websites and WikiNews, among other similar products, have helped to address certain aspects of this issue; I believe that the platform presented here will help to create a more robust solution that fills the gaps between these services by providing one centralized website network that supports all steps of the journalism workflow. Leveraging the power of crowdsourcing and real-time collaboration will help to produce sustainable, long-term availability of relevant local news to all citizens.

### References

Barnett, Steven & Townend, Judith. “Plurality, Policy and the Local, Journalism Practice,” 2015, 9:3, 332-349, DOI: 10.1080/17512786.2014.943930

Bercovici, Jeff. “The Fatal Error That Doomed AOL’s Patch.” Forbes, 16 Dec. 2013, https://www.forbes.com/sites/jeffbercovici/2013/12/16/the-fatal-error-that-doomed-aols-patch/.

Carr, David. “AOL Chief’s White Whale Finally Slips His Grasp.” NYTimes, 16 Dec. 2013, https://www.nytimes.com/2013/12/16/business/media/aol-chiefs-white-whale-finally-slips-his-grasp.html.

Lewis, Seth C., Kaufhold, Kelly & Lasorsa, Dominic L. “Thinking About Citizen Journalism,” Journalism Practice, 2010, 4:2, 163-179, DOI: 10.1080/14616700903156919

Mitchell, Amy, et al. “How Americans Get Their News.” Pew Research Center's Journalism Project, Pew Research Center, 14 July 2016, www.journalism.org/2016/07/07/pathways-to-news/.

O’Connor, Rory. “Can Citizen Journalism Work?” The Guardian, 5 July 2007, http://www.theguardian.com/commentisfree/2007/jul/05/cancitizenjournalismwork.

Scott, Jonathan; Millard, David & Leonard, Pauline. “Citizen Participation in News,” Digital Journalism, 2015, 3:5, 737-758, DOI: 10.1080/21670811.2014.952983

Wall, Melissa. “Citizen Journalism,” Digital Journalism, 2015, 3:6, 797-813, DOI: 10.1080/21670811.2014.1002513
 “What Is Patch?” Patch Support, Patch, http://patch.zendesk.com/hc/en-us/articles/115000876891-What-is-Patch-.
 
“Wikinews: Introduction.” Wikinews, Wikimedia Foundation, Inc., http://en.wikinews.org/wiki/Wikinews:Introduction.

St. John III, Burton; Johnson, Kirsten & Nah, Seungahn. “Patch.com”, Journalism Practice, 2014, 8:2, 197-212, DOI: 10.1080/17512786.2013.859835
