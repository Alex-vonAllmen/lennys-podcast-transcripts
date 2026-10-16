---
guest: "David DeSanto"
title: "The GitLab way: Kindness, transparency, and short toes | David DeSanto (CPO)"
publish_date: "2024-04-14"
source: "https://www.lennysnewsletter.com/p/the-gitlab-way"
slug: "the-gitlab-way"
archive_id: 142957811
topic: "The GitLab way: Kindness, transparency, and short toes"
description: ""
summary: ""
youtube_url: "https://www.youtube.com/watch?v=cJo2Yf5UOEU"
video_id: "cJo2Yf5UOEU"
duration_seconds: 4893.701
duration: "01:21:33"
channel: "Lenny's Podcast"
transcript_source: "substack-transcription"
---

# The GitLab way: Kindness, transparency, and short toes | David DeSanto (CPO)

## Transcript

Lenny Rachitsky (00:00:00):
You guys share so many of the things that most people keep secret. You post videos of your team meetings on YouTube.

David DeSanto (00:00:05):
We get people who then contribute because of what they see. "Oh, I can go build that. I know what that is. Hey, I ran that same problem too. I'd love to hear how you solved it."

Lenny Rachitsky (00:00:13):
You also have this handbook, how you onboard people, how account payables works.

David DeSanto (00:00:17):
At GitLab, we'll have companies who will fork the handbook. If you can leverage what GitLab has done, that's amazing.

Lenny Rachitsky (00:00:24):
You mentioned the value of short toes, which I was definitely going to ask about.

David DeSanto (00:00:27):
That's where if you have long toes, you feel like people are stepping on you, whereas if you had short toes, it's about the work, it's not about you. You end with a lot less of the negative headbutting, especially in an asynchronous culture like GitLab.

Lenny Rachitsky (00:00:38):
Is there any tips you could share with PMs that are just struggling in a remote world?

David DeSanto (00:00:42):
If everyone's really annoyed at you, you're probably actually doing your job well.

Lenny Rachitsky (00:00:49):
Today my guest is David DeSanto. David is the Chief Product Officer at GitLab, which is an incredibly unique company. It's the largest remote-only company in the world. They share many of their team meetings on YouTube and they've grown from being just a source code management business competing with GitHub to a multi-product platform that covers security, compliance, continuous integration, project management, deploy tools and more, many of which are infused with AI magic. In our conversation, we dig into GitLab's culture of transparency, including how they operationalize it, what they share publicly versus what they don't. The surprising benefits of working this way and why it's worth considering going transparent with your organization. Also, explore some of GitLab's other unicultural values like kindness and having short toes. Plus, David shares a bunch of great advice for scaling remote work based on what's worked well at GitLab over the years. Also, when it makes sense to go breadth over depth versus depth over breadth when launching new product lines and how it worked for GitLab over the years. This was a fascinating conversation and if you want to learn more about a company that's doing things very differently while also kicking a lot of ass, this episode is for you. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It's the best way to avoid missing future episodes and it helps the podcast tremendously. With that, I bring you David DeSanto after a short word from our sponsors. This episode is brought to you by Orb. As a business, you care about revenue, but as a product team, the last thing you want to do is delay a product launch or a pricing change because your team has to rebuild billing from scratch. Orb is a flexible usage-based billing engine that lets you evolve your pricing with ease. The fastest growing product teams at companies like Vercel and Replit. Trust Orb to power their pricing changes and launches. Use Orb to ship product faster, stop worrying about billing and evolve pricing with ease and control. Check it out at withorb.com/Lenny and skip the line for demo or sandbox by using promo code Lenny. That's withorb.com/Lenny. This episode is brought to you by Eppo. Eppo is a next-generation, A-B testing and feature management platform built by alums of Airbnb and Snowflake. For modern growth teams, companies like Twitch, Miro, ClickUp and DraftKings rely on Eppo to power their experiments. Experimentation is increasingly essential for driving growth and for understanding the performance of new features. And Eppo helps you increase experimentation velocity while unlocking rigorous deep analysis in a way that no other commercial tool does. When I was at Airbnb, one of the things that I left most was our experimentation platform. Break it, set up experiments easily, troubleshoot issues, and analyze performance all on my own. Eppo does all that and more, with advanced statistical methods that can help you shave weeks off experiment time and accessible UI for diving deeper into performance and out-of-the-box reporting that helps you avoid annoying prolonged analytic cycles. Eppo also makes it easy for you to share experiment insight through your team, sparking new ideas for the A-B testing flywheel. Eppo powers experimentation across every use case, including product growth, machine learning, monetization, and email marketing. Check out Eppo at getEppo.com/Lenny and 10X your experiment velocity. That's geteppo.com/Lenny. David, thank you so much for being here. Welcome to the podcast.

David DeSanto (00:04:24):
Thank you for having me. Very excited about our chat.

Lenny Rachitsky (00:04:27):
I'm very excited as well. You definitely win for best beard of any guest of the podcast so far. What does it take to maintain such a beard?

David DeSanto (00:04:36):
That's a great question. So I would tell you it's not as much as you think it would be. It's just regularly going to a barber you trust that can keep the shape and it does get washed and conditioned regularly because my hair migrated south for the winter, never came back. And so it's become the staple. So yeah, comb it, put conditioner in it, things like that. Not a lot of maintenance, surprisingly.

Lenny Rachitsky (00:05:01):
Okay, and I think you mentioned offline, your handle, is it on Twitter? What is it?

David DeSanto (00:05:06):
Oh, so I just started trying to use threads and-

Lenny Rachitsky (00:05:09):
Oh threads. Okay.

David DeSanto (00:05:10):
Everywhere else I'm like D DeSanto or David DeSanto. Those weren't available so I'm David The Beard, david.the.beard.

Lenny Rachitsky (00:05:18):
Amazing.

David DeSanto (00:05:18):
So you can all follow me there once you watch this because I think I've got 10 followers in the first couple weeks here. I would love to get it to a much higher number so you can help with that.

Lenny Rachitsky (00:05:29):
Okay, let's work on that. And then if you're not watching on YouTube, you're missing this beard. Anyway, I'm excited to have you here because I've always been really fascinated about GitLab's culture. There are so many unique elements to how you guys operate and clearly it's worked out really well. The company has just, looking up, the stock is a $11 billion business at this point, it's been around for a long time. So I want to dive into a number of the different ways that you guys work, especially the stuff that's really unique. And the first element is your very unique culture transparency. I have not seen anything like this elsewhere. So first of all, as an example, you post videos of your team meetings on YouTube?

David DeSanto (00:06:06):
That's correct, yeah.

Lenny Rachitsky (00:06:07):
Okay. And I want to chat about what the policy, but just as an example, I was watching a product team meeting of your product team a while ago where they're talking about a book club of Marty Cagan's recent book. I was watching engineers talking about some scaling challenges they were having. There's a video of you being introduced to the UX team from a year or two ago and maybe it was after a reorder or something. What's just the policy on which videos go online?

David DeSanto (00:06:30):
Yeah, so that's a great question, and you're actually correct. So about two years ago we moved UX from engineering into product to make them a much more strategic part of the company. I knew a lot of UX but didn't know everyone in UX, so we took the time to let me introduce myself to them if they weren't familiar with me or hadn't talked to me at all. But to your question, our policy is be as transparent as possible. So if it's not customer data, it's not vulnerability information. We heavily encourage the team to put their videos, record the videos, sometimes even live stream them onto our YouTube channel. So for those not familiar, you can search GitLab and filter it on YouTube and there's more content there than a human being could watch in a single day or even everything that's recorded during the day. There could be multiple meetings happening at once that are also showing up there. But a good example of that is my bi-weekly product meeting where we go over things we're working on, things we're excited about troubles, we're having challenges in how we can work better together. I can tell you that it was a change during GitLab in 2019 to have that much content just be available. You also learned how to be better on meetings because of it. My first meeting was my first day and I spent a lot of time looking all over the room because I was used to being on a Webex where you can't see anything, so you could be looking outside while talking and all of a sudden you realize you're not really engaging because you're assuming it's just an audio call. And so I think it's been really good for the company. The great example I can give you is we get people who then contribute because of what they see. And so we've had customers, open source community members go, "Oh, I can go build that. I know what that is," and they will just knock it out and do a code commit. Or we will get feedback on the video or feedback on social media. It's like, "Hey, I ran that same problem too. I'd love to hear how you solved it." And so I think it's been really great for not just the company but the broader community, whether they are paying customers or open source contributors.

Lenny Rachitsky (00:08:33):
So just to understand, there's developers watching team meetings, noticing there's like a bug or an issue or a challenge and then just going ahead and committing code to fix it.

David DeSanto (00:08:44):
So sometimes there'll be open source community contributors who are doing that. So yeah, they'll hear about that. They'll look at the issue tracker because the issue tracker is all public and they'll just be like, "Oh, I can do that. Let me just do that and make the project better."

Lenny Rachitsky (00:08:58):
Oh my god, that's crazy. Okay. And so the policy as you described is it's up to the person, they decide is this something we can share that feel comfortable with?

David DeSanto (00:09:06):
Yeah, it's up to the person and the team. So I do have a couple policies for the product division where we don't post the recording. We used to do live our, what we call our performance indicator reviews and key reviews. We stopped putting those public because we want to talk about the customer that's impacted or we want to talk about the thing that we need to move. And so we'll talk about it at a high level in our product division-wide meeting that is posted, but then the nitty-gritty down details that would be considered material nonpublic information or customer data that would need to be kept safe. Those things, we will record those but keep those internal and not make them public.

Lenny Rachitsky (00:09:49):
Okay, amazing. So you have these videos. You also have this handbook, the GitLab handbook, which is handbook.gitlab.com, which also shares tons of pieces of how you all operate. So just skimming through it, there's your mission, your vision, your strategy, how you onboard people, your anti-harassment policy, how count tables works at GitLab. Hilarious, amazing stuff.

David DeSanto (00:10:11):
It's great too. I don't remember how many pages it is now, but it's huge. And so what I see what happens, and this gets into the first example, we'll have companies who will fork the handbook. It's just source available too. At the bottom of the page you can click view source. And I just heard from a company who's now becoming a customer who were like, we wanted to redo our UX mission and how we operate in a UX department. So we cloned the UX handbook within handbook.Gitlab.com and it became our baseline for building what we do. And you can see that even for startups, we will say they've cloned the entire handbook and they use it as a way to start. And I think for me, across my career, I've been in this situation where I needed to fix something or restart something or I'm the first person in the department and there's a lot of uplifting you have to do in that role. Whereas if you can leverage what GitLab has done, that's amazing. It really helps you continue forward really quickly.

Lenny Rachitsky (00:11:15):
Yeah, I think one of the most interesting for me has been the competencies for product managers. Something a lot of PM teams are looking for is how do we level and ladder and create levels for teams? And you guys share all that and you guys have a really good version of that publicly. So we talked about the YouTube. I have a bunch of questions about how this actually works, but so you have the YouTube channel of team meetings, you have the handbook. Is there anything else that I'm not mentioning that's public that other companies don't share?

David DeSanto (00:11:41):
I think there's really two things. So the first one is our issue tracker for everything we're doing. The majority of those issues are public. It's also available for people who have an account to also create and comment on. And so whenever we do a call with a customer or I present at a conference or my team presents, we always say, "Hey, please go look at our issue tracker and if there's something you like, vote it up. If there's something you want to see change, leave a comment." And I think that's unique to GitLab. I think we've actually caused other organizations to do something similar because of that. And the other one is our direction and our strategy. You mentioned earlier, sometimes it's just a high level paragraph, but sometimes if you go deeper, we have a one-year direction that is very detailed and links over to our issue tracker to help you see, "Hey, we're going to do, I don't know, we're going to build widget X and we're going to do it in the next six months and here's how we're going to do it." And I think all those things together have really allowed GitLab to be the most transparent publicly traded company in the world. And we're very proud of that because it's just in our DNA to do it.

Lenny Rachitsky (00:12:49):
I think what's really interesting about this is it's the epitome of, it's not the idea, it's the execution. You guys share so many of the things that most people keep secret and it's worked. I guess is there any lessons there of just like, it's actually a lot, the execution is what's separates you from everyone else. Someone could just basically copy everything you're doing in theory, build something like you built, but they haven't.

David DeSanto (00:13:12):
Yeah, I think you're touching on actually when I interviewed in 2019, I actually asked Sid, our co-founder and CEO, a similar question. And I came from security in the GitLab and I said, hey, we don't share more than four or six weeks with a roadmap with customers and even sales because we were in the situation where we didn't want our great idea to be taken and built before we built it. And that had happened to me at other places I've worked. And so in that conversation with him, he basically said, "It's product's job to be ambitious instead engineering's job to meet that ambition." And if you think of it that way, and it's that collaboration between the two, it becomes less scary to put the information out. But you are right. We're very even transparent there. The thing that gets into what you mentioned, the ability to ship software, I'm floored by these numbers, but these are real numbers for us. We still ship 12 releases a year. It used to be on the 22nd of every month, it's now the third Thursday, so we don't have to have people work over a weekend, but we've done that for over a decade. And our last release put us at 149 releases that have come out essentially every month for the last little over 12 years.

Lenny Rachitsky (00:14:29):
Someone listening to this may be like, okay, wow, we should try this sort of thing. Let's try to be transparent with everything, meetings everywhere, public handbook. Imagine this doesn't work for most companies. So a question just on my mind is, what do you think it takes for a company to work this way? What are some elements that need to be true for them to succeed being this transparent?

David DeSanto (00:14:53):
Yeah, I think it is pushing yourself to realize what is actually confidential and what actually is not confidential. At other places I've worked, they end up with these artificial silos even if you're all in the same office. And that ends up impacting your ability to truly collaborate and get the results you're looking for. And I can give you a great example that sometimes you have a program manager or program management team who's tracking the schedule and now they're being forced to be the router between teams, as opposed to say it's all stored in a single source of truth. Anyone can comment on it, anyone can contribute to it. And that starts all the way from team meetings, whether it's my leadership team or it goes all the way down to coffee chats that we have where sometimes people will just record that chat because all of a sudden there's something really interesting in that. And for those listening or watching us, as you said, looking at the beard that I have instead of just listening to the podcast-

Lenny Rachitsky (00:15:52):
I think they can hear the beer too.

David DeSanto (00:15:56):
It gives me presence. So yeah.

Lenny Rachitsky (00:15:59):
Makes your voice deeper.

David DeSanto (00:16:00):
There you go. So what ends up happening for us, a coffee chat is the equivalent of walking in and running someone in a kitchen so you're getting more coffee or tea or water. And so sometimes those just end up getting recorded because there's something that's a good nugget of information that comes out of it. And so realistically you just have to push yourself and it almost has to be uncomfortable. And then you realize you're starting to really truly be transparent and you're allowing everyone to contribute.

Lenny Rachitsky (00:16:30):
I imagine this isn't all upside and rosy and rainbows all the time. Is there anything that you've heard of or ran into where this caused a problem either for the company or someone internally?

David DeSanto (00:16:40):
Yeah, that's a great question. So I think if you go back to the, you have to push yourself to your uncomfortable. Sometimes that ends up being overly transparent and GitLab has had its fair share of things at times where an issue is public that probably shouldn't have been public, like our issue tracker or the recording accidentally gets set to public when it should have been set to private. And those are just pain points and learning. And then as long as you're reinforcing that learning across the team, you end up not making that same mistake again. And I will say that, I think the risk that occasionally happening is way below the value of actually pushing yourself to do it. So what I would encourage you to do is start as simple as publishing a team meeting and making that available for everyone in the company. Begin to go from there to maybe weekly meetings or even asynchronous readouts that you can post on Slack that are just saying like, "Hey, here's everything that happened this week with the team." And then you'll slowly find that if you're doing it, others start doing it. And before you know it, you've actually achieved a high level of transparency. Now, depending on the industry you're in, maybe you can't make your issue tracker public. If you're like GitLab and you're using GitLab.com, maybe you can't share the details we share about customer meetings and our conversations with them, obviously without saying their name, but you'll find the right balance for you and I think you'll truly find that as a company you become more productive.

Lenny Rachitsky (00:18:11):
To convince someone that this is worth doing, what do you find are the biggest benefits of operating this way? It sounds like more work and it sounds like there's more risk. And so what do you find are the benefits and also just maybe second order benefits that you didn't directly expect?

David DeSanto (00:18:27):
Yeah, so I would say the big thing I've seen is focus on results, especially for our customers. We are a global company. We weren't always as big as we are, but GitLab is over 2000 people. It allows people to asynchronously consume what happened while they were offline and it gives them both more engagement as well as that lack of feeling of FOMO or fear of missing out. And to me, those are really the top level items that come out of it. The secondary benefits of those are of course teams feel better aligned. You find things that you may not find until the end of a software release or beginning of a go-to-market campaign. You have to redo something. And so I just think really, and I say this with encouragement to people, pick one project and try it. And if that's successful and doesn't feel like a lot of additional work, try it with another one. And before you know, might find out that it's actually a lot easier to be transparent than it's to not be transparent because now you don't have to worry about tracking things you may or may not have said. Think about, well, did this person hear it or were they not in that meeting? It just becomes that that's a lot of data that people can consume and then they can make informed decisions quicker because they're not being siloed out of the conversation.

Lenny Rachitsky (00:19:43):
Well, it feels like there's two elements here. There's being transparent internally with here, you can listen to every meeting that you've had as an employee, but where you guys go is one step further is anyone can pay attention to this and read your handbook. What do you find are the biggest benefits of that element, of just being public about this stuff?

David DeSanto (00:20:00):
Yeah, for me it really comes down to the engagement we can get externally because our issue tracker is public, our customers comment on it, we get community contributors committing to our code base and helping get that to be a better product. I can see where in certain industries we'll say financial services, maybe you can't do that as much, but I would say that there's still a balance where there's probably something you'd be more transparent about. I'm even seeing in heavily regulated industries where they're starting to publish more of the roadmap externally as a way to build more trust with their users and their customers because now they know where you're going and it's not a cloak and dagger type feeling. And so I will admit it can't be done everywhere, but I think it can be done a lot more than it's done today and you get a community feedback loop, which is great, especially when being in a product division.

Lenny Rachitsky (00:20:52):
So one takeaway here is it feels like most of the benefit is in products that are building with a community component and developer oriented and open source. Feels like those are the Venn diagrams of where this is most impactful versus Slack doing this or I don't know, Salesforce.

David DeSanto (00:21:12):
Yeah, I would say that if you're in tech and you're building a product regardless if you're a developer platform or a DevSecOps platform like us, I think there is benefit. I think Salesforce could have a little bit more engagement from a broader customer base. My last employer, we started sharing the list of open requests for new features more externally and we got a much more honed in roadmap and that led to better customer engagement, which led to a higher retention rate, which led to better expansion numbers. So I think it's about what's right for your business and not necessarily are you in column A or column B.

Lenny Rachitsky (00:21:53):
I was browsing around through the handbook and I looked at your core values and there's some really sweet things in there. So within the collaboration core value, there's a value of kindness, which I love. What does that look like in practice at GitLab?

David DeSanto (00:22:09):
The values really come together in a way that I've not seen other company values come together, and I don't remember where these all are in there, but it ties into the kindness. If you're all remote, you're not necessarily seeing people in person and sometimes it's hard to read intent on a Slack message or the emotion in the message. And so we say assume positive intent, assume the person is traditionally just asking for help or is trying to be helpful. Have short toes, don't read something and think it's meant a different way. And that's where the kindness comes in as well, is that if you're treating each other with kindness and assuming positive intent, you end with a lot less of the negative headbutting you can have, especially at an asynchronous culture like GitLab. Our team, I will see my direct reports usually at least a couple minutes a week on a Zoom call, but that's not the case for everyone at GitLab. And same thing with other teams, and sometimes it's hard to assume what the person's intention actually is. And so we say, "Be kind, assume the positive intent, realize that everyone's here to help each other out." And I can tell you when people ask me what's it like working at GitLab, I always come back to the values and say we actually live them. And that starts with Sid all the way down the organization to a brand new employee straight off college. If we're doing that, then there's a lot less of that tension and headbutting that can happen in organizations, especially when we don't see each other all the time in person.

Lenny Rachitsky (00:23:42):
Some of the other elements along the be kindness is say thanks and say sorry, and negative feedback is one-on-one.

David DeSanto (00:23:49):
Yeah. By the way, for those who aren't looking at the values, you can go to aboutGitlab.com/values and you can see them. But what I will share with you is that we have a thanks channel where people just post a thank you note whenever they are truly thankful for something and that channel is constantly getting those messages in and it's reinforcing that engagement that you really want to have where people are working together collaboratively and assuming positive intent and so forth. But I'll tell you the negative is one-on-one that you mentioned, that one's actually really important to me because you don't want someone to take a public message the wrong way. And so you take that conscious step to say, "Hey, I got to give that feedback, let me do that one-on-one." And that means if it's in a public channel, it's even easier to assume the positive intent because negative feedback should be one-on-one.

Lenny Rachitsky (00:24:40):
Yeah, I think the more you talk about this and we're going to talk about remote work, it all works together. Remote work almost forces you to be very specific in how you communicate, be transparent about all the things going on at the company. So this all makes a lot of sense as this flywheel I imagine that kicks in.

David DeSanto (00:24:54):
I agree with you. I think you can't be as transparent as we are without having our values. You can't have our values unless you're trying to put it sometimes into the remote work environment and vice versa. And I think they all fit really well together and it's been the company continuing to grow and adapt them as we've gone from, again, one person to over 2000.

Lenny Rachitsky (00:25:16):
You mentioned the value of short toes, which I was definitely going to ask about. Talk about what that means.

David DeSanto (00:25:22):
So the short toes is, it's about the work, it's not about you. And so if you have made something and you're getting feedback on it, try to realize that as someone trying to help you make it better and not a personal view of how you are as a person or as an employee. And so a great example would be, I make videos occasionally and post them on Slack and people can consume them, and those are not always well received. I don't take that personally, I take it as an opportunity to say, "What could have made this video better so the next time I do it provides a lot more value." And I think that is really where that short toes comes in. It's about comment on the work, not the person. It's not, "Look what you did." It's like, "This could have been better this way." And if you're assuming positive intent, having short toes, you end up having less headbutting.

Lenny Rachitsky (00:26:15):
I think the implication here is that you don't want to feel like people are stepping in your toes. Your toes end up being short. That's where this comes from, I imagine.

David DeSanto (00:26:23):
It does. And part of that ties back to those other values. You aren't your work. So if someone's reaching over and doing something in your space, that's where if you have long toes as they're called, you feel like people are stepping on you. Whereas if you had short toes, it's about contributing and so forth.

Lenny Rachitsky (00:26:45):
It's so funny. I love the way of describing it. And it's the exact opposite of Uber who's one of their values I think was encouraging toe stepping. Step on toes, don't worry about it. Long toes.

David DeSanto (00:26:56):
Our approach was to take the other side of the move fast and break things. It's more about building that community, that trust and everyone hitting the results together.

Lenny Rachitsky (00:27:07):
Sounds like a delightful place to work.

David DeSanto (00:27:09):
This is the happiest I've been in my career. It has nothing to do with my success at GitLab, though I'm sure that's part of it. But it's also, I know that we're all working together for the common good. We're all trying to aspire those values and it makes it a great place to work. And it's been the happiest I've been, and I've been here four and a half years.

Lenny Rachitsky (00:27:28):
Wow. I love hearing this and it's done great also. It shows that you can build a very successful business and people can be very happy. What a rarity.

David DeSanto (00:27:39):
Yeah. No, agreed.

Lenny Rachitsky (00:27:41):
Are there other values that you find to be really core to the way GitLab operates that I haven't mentioned?

David DeSanto (00:27:47):
Yeah, I think for me it's the results and the efficiency ones that always hop out for me. And results is focused on results for customers, and that's why we do everything we do. Almost any company that's really the case. And so how do we help our customer get their software ship faster, make their software more secure, give them better visibility into its usage, and having that focus on the customers, the number one thing, it allows us to be a lot more empathetic with not only our customers but the broader community. And efficiency is really about how do you get work done? And we try to drive responsibility down to the lowest level in the organization. I, as the leader of product will set a three year, seven year strategy, but how we get there, we leave up to the individual teams and that empowers them to be able to work efficiently and hit that high level of velocity that we talked about at the beginning of our chat. And so I think for me, those things come together. It's okay to ship something that you think is good, but maybe it's not great yet. Get it out there, get that flywheel working so you get the feedback from the customer and then iterate on it. And I think those two things together on top of what we talked about, the transparency and the collaboration really help us be who we are today.

Lenny Rachitsky (00:29:07):
Did you say a three year and seven year vision?

David DeSanto (00:29:10):
Yeah. We have on the website up to I think a 30-year mission. So we have our mission, we have our vision, we have our strategy, and we have our direction. Those are the levels of which we plan.

Lenny Rachitsky (00:29:21):
What's the thinking there?

David DeSanto (00:29:23):
The thing is to make sure we're always going towards where we think our customers are going to need. And so to give you an example, the three-year strategy says our goal is become the first all ops platform. And that essentially to say that we want to be the single source of truth for RD organizations, and that's not just the people who are in R&D like product, UX, engineering, infrastructure, but for the teams that work around them including legal, sales, product marketing, compliance and so forth. For us, all ops means it's everything that's needed to do that. That's what we've built, not just source code management and code review and so forth or CICD. We've added security and compliance, we've added enterprise-led planning. We're even starting to add service desk service management functionality in GitLab as well. So for us, that's our long-term goal. And then we empower the teams to get there the way they think we need to get there for their area or a new area that needs to be created. For those who are not as familiar with GitLab, we're structured by sections. Those are areas like dev, sec and ops. Those have stages in them that map the DevOps tool chain, like create plan, monitor, verify, and then those have groups in them. And those groups are that lowest group I'm talking about where we've pushed on the priority and those will be the things that have our categories. So there's a group that's called environments that manages our Kubernetes integration, our deployment dashboard and so forth. And that of course then all feeds back up to that top level vision. And so it's allowed us to be structured in a way that helps us ensure that the people who need to work closely together can across those groups, and allows us to tie stages together to make sure we're hitting the outcomes that we need. And so that is how that all then fits together. There's a group direction, there's a stage and section strategy, and then there's longer-term vision and then mission.

Lenny Rachitsky (00:31:19):
And I love that all of this is there in the handbook. You can see all this and then you can also see your cadence for revisiting it, planning team meetings, executive staff discussions.

David DeSanto (00:31:29):
And by the way, we also put, that's all the way down to the group level. So on our marketing site, if you go to aboutGitlab.com, again /direction. Under direction is the product direction that we've set for the next year. And then that links out to those stages and groups so you can really follow along. And when you get lower into that to the group level, they're linking to their epics, their issues and their tasks. And our issue tracker so you can easily find them. We have I think 72,000 open issues right now in our backlog and it'd be hard to dig through all of that. It's people creating new ones, customers commenting on it, just keeps the backlog really large, but you can go through that marketing site that we have and get to the thing you're actually interested in reading about.

Lenny Rachitsky (00:32:12):
There it is. I'm looking at it. I love it. When someone joins GitLab and things don't work out, they don't end up being a fit. Other than them not just having the skills they need, what do you find is the most common reason for them not being a fit at GitLab?

David DeSanto (00:32:29):
So I think it really dialed into the remote experience. Remote is not for everyone and we'll have people who come and they're really great. They don't even have to be an under performer, but they're missing that in-office every day feeling, maybe in some cases they just want to get out more and be not at their home or at the same coworking space all the time. And so for them, that's really the thing. The thing for them is that they just don't feel connected the way they want to be connected. I'll be honest, I started at GitLab a couple months before the pandemic. For me, I got to attend our sales kickoff, but that was only a third of the company. And it's not until actually in March this year that we're doing our first company-wide get together where I'm going to get to meet some people I've never had the chance to meet in the four and a half years I've been here. And so I myself found that a little jarring initially, I worked in a company that had a hybrid model and I knew what that was like to have people not with you. But the fact that human connection can be missed more so for some people than others. And I think that's really what it comes down to, yeah, you're right, they could not understand the technology. Maybe they're not fitting into their role, but I think sometimes it's also I am not enjoying the all remote, I'll call it lifestyle. It is an adjustment to how your day goes and how you engage and all that sort of thing.

Lenny Rachitsky (00:34:05):
That makes sense. And that's a great segue to where I wanted to go, which is talking about remote work. So I think you might be the largest all remote company, do you think, is that true?

David DeSanto (00:34:14):
We were pre the pandemic when we were around 1100 people. I think everyone now having recalls back to the office, we might be back to being the largest all remote. I've not seen a number yet that from other companies, how much are they still remote, but obviously during the pandemic, I think Google and Apple would win as the largest all remote. Whereas yeah, now those people are coming back to the office, we might be back to being the largest.

Lenny Rachitsky (00:34:42):
Okay. And I think even if you aren't currently the largest, it feels like you will be probably long-term because people go there and then move back. Also, GitLab has been doing this way before school, way before everyone else started to try to go down this direction. It feels like there's a lot that people can learn from how to work remotely successfully. I'm curious, when you talk to other leaders and other companies that are trying to improve the way they work remote, what advice do you share? What tips do you have for making remote work more effective?

David DeSanto (00:35:07):
Yeah, I think there's a handful of things that I really encourage people, which by the way, I do get reach outs on, it's now called X, LinkedIn where someone will say, "I read this in the product handbook, but I don't understand how this then applies in an all remote environment." And so I usually say, if you're looking at being a remote first culture, there's a couple of things you just need to understand and focus on. Things like be transparent. We've talked about that a bunch already. Focus on results, not hours. Sometimes people get fixated on the, "Well, did you work the full 40 hours this week? Or Wow, you worked more than 40 hours this week, what's going on?" And instead it should be about, "Hey, we've agreed to an outcome and have we achieved that outcome?" I think over communication's also key that I share with people. The best way to put is, I have an executive coach. He's a great guy. One thing he said was that if you think you're communicating a 100% accurately, that's probably 60 or 70% for the other person, and shoot for 150%. And so that's something that I think really helps in that environment. And then lastly, and we just talked about this is making time for in-person events. I have my leadership team get together every quarter. Every other quarter of that we bring in our director plus group and we're actually doing that next month. Last time we did it was in October. And see if you can find ways to get more part of the team together. I just shared we're having our first company-wide get together since the pandemic, but that doesn't mean that we had to wait that long. I got the product division, all 140 of us together, across two different cities over the course of a month to allow people to finally get to meet each other and make that human connection. I think when someone gets to do that, it makes Zoom feel a little less scary because you've actually seen and maybe hugged or shook the hand of that other person and now you've got that same human connection that you may not otherwise get if you just never saw your coworkers in person.

Lenny Rachitsky (00:37:15):
So the four pieces of advice you shared, transparency, spend a lot of time just being more transparent, focus on outcomes versus quality, quantity of hours. Over communicate and make time for in-person. Within the outcomes bucket, a lot of people like, yes, it sounds great, we will focus on outcomes. We're not going to think about how many hours you're working. It's hard to do a lot of times because in this sort of work it's like I don't know, what should I expect of this person to achieve? Maybe this bug takes a week, maybe took a day. Do you have any just advice to help figure out and nail, here's how we can create outcomes that connect well with people actually working fully?

David DeSanto (00:37:56):
Fixing a bug is more of a deliverable than a business outcome. And so we try to make them things like, we want to have 60% of our customer base using this part of the portfolio. Now what do we do to get there? And that allows people then have a measurable outcome that does tie back to how many hours they're working to a degree, right? Because scoping it. But it's not about the ship 20 features next month. That could take you more than a month. That could take you a day and a half if you break down your feature into tiny little features. Whereas it's more like celebrate the adoption, not the shipping. And I think that's really where we've tried to move. GitLab as a company has always been very focused on how fast we ship software, but that's not really how our customers use it. It's more about what pain point or use case did we solve? And if you're now framing it in that way, you begin to move away from the deliverable and the hours and you get into the, did the customer adopt it? What was their outcome? What success did they have? What are you trying to do with that? And by the way, I think that's the biggest challenge for people who move from a different role into a product division or a product role, is changing that dynamic to not be the bits and the bytes but be the use case, the pain point. Because sometimes you actually don't need to ship a new feature per se, sometimes you just have to make it more usable and then all of a sudden you're getting the outcome you're looking for.

Lenny Rachitsky (00:39:31):
You said that a lot of people reach out to you and try to dig into some of the things you do. What are some of those most common questions people ask you and or where do people most often go wrong when they're trying to work the way you all work?

David DeSanto (00:39:43):
Probably the top topics that people reach out to me for, the first is how did you get into product? Because my background, I started as a software developer, had my own company, sold it. For all those listening, just enough to pay off its bills. It was not like I am independently wealthy now. And moved into security research and eventually into product. And it's like, "How did you make that leap? How did you know it was the right thing for you?" The next topic is the, "I see GitLab has this very transparent handbook and this GitLab unfiltered channel. How did this happen? Why are you doing it?" And then the last one's usually, "How do I know remote development is for me and I make the jump." And I talk about myself and my time in the office versus not in the office. And the thing is, for me, I was very transparent with the team when I started in 2019 that I'm like, "This makes me a little freaked out. I'm not sure this is going to be the thing for me." And I love it now I can't imagine not doing it. I like to look back at that time when GitLab made the offer to have me come in and start leading a part of the product division and my wife saying, "You're going to love this. I don't know why you're questioning it." So listen to your friends, your family, your partner. They can also help you with that sort of decision.

Lenny Rachitsky (00:40:59):
This episode is brought to you by Paragon, the embedded integration platform for B2B SaaS product development teams. Are your users constantly requesting new integrations with other SaaS platforms that they use? Unfortunately, native product integrations take months of engineering to build and the maintenance never ends. Paragon enables your engineering team to ship integrations seven times faster than building in-house by removing the complexities around authentication, messy third party APIs and debugging integration errors. Engineering teams at companies like Copy.AI, Cinch, TLV and over 100 other SaaS companies are using Paragon so they can focus their efforts on core product features, not integrations. The result, they're shipping integrations on demand, which has led to higher product usage, better retention and more customer upsells. Visit useparagon.com/Lenny to see how Paragon can help you go to market faster with integrations today. That's useparagon.com/Lenny. Let's do a quick tangent on that first bullet you mentioned of getting into product. What advice do you share with people that are just like, "Should I get into product? How do I get into product?"

David DeSanto (00:42:11):
I am very transparent that product is not necessarily the rock star role that people think it is. The way I tell people who are doing their career, maybe they're now an associate or intermediate PM at GitLab or other places I've worked that if everyone's really annoyed at you, you're probably actually doing your job well. Product is the hub in the middle of the wheel and the spokes are engineering, marketing, sales, legal and so forth. And they can't do your job unless you're properly leading. And if you're pushing the boundary and they're all getting a little like, "Are you really sure that's what you want to do?" Or "Wow, that seems like a lot of work." Or "Huh, I hadn't thought about it like that." You're probably doing your job well. And what I encourage them to do is think outside the box, not focus on the, I call it order taker or deli counter worker and the US where everyone gets a number and you just fill what that is. Think about what do all those requests together really mean and then do that and not take the orders. And so, that's the advice I give, is like, it's not the big sexy role that everyone talks about. It's actually a lot of work, a lot of discussion, sometimes tension and lead with the customer first and the use case and the pain point and then everything else will fall in behind that.

Lenny Rachitsky (00:43:37):
I completely agree. It's the most thankless painful job there is, but also the best job.

David DeSanto (00:43:42):
Yeah, I now have been doing for a while, I can't imagine not being in product. And so I'm glad I made the change and I've not looked back.

Lenny Rachitsky (00:43:52):
Specifically with PMs in a remote culture. I never worked in the remote world as a PM. COVID happened after I left the field and started doing this crazy weird job. Is there any tips you could share with PMs that are just struggling in a remote world where it used to be, you just walk up to an engineer, "Hey, how's it going? How's this thing looking? Let's check out this design." You have any advice for just how to do those sorts of micro interactions and stay on top of things?

David DeSanto (00:44:15):
Yeah, there's probably two or three points I would make. The first is, if you're in an all remote world, your requirements have to be clear. Sometimes you can get away with, "Hey, I have a daily stand-up or a couple weeks stand-up." And then you use that as the opportunity to clarify something. You have to get it written the first time or at least refined before you expect someone to work on it. And so as part of the interview process at GitLab, we do what's called a deep dive interview where we have the person try that out and they engage with another person or product who's playing the engineering side of that conversation. And it really helps both us see whether or not the person has the potential to be able to work in that type of environment.

Lenny Rachitsky (00:44:57):
Oh, this is part of the interview process?

David DeSanto (00:44:59):
In the interview process, correct. And then it also gives them the opportunity to decide, can they actually do it? And we've had candidates who go like, "This wasn't for me." And so that's the first thing is writing real concise requirements is really key.

Lenny Rachitsky (00:45:15):
Just understand before we move on, so in the interview, so what is it that they do? You ask them here, write the requirements for this feature that we have and then they do a role play as part of the interview with an engineer asking them questions about it?

David DeSanto (00:45:28):
So it's actually they can write requirements for anything. We are not using it as a way to get free requirements written up as part of the interview process. So one candidate, their topic was they chose bicycles and so it's like you're going to ship a new bicycle, then what's the epic, the higher level vision and what's the first milestone for us milestones or releases? But that first iteration, what is the NBC for that or minimum viable change towards it. And then they create that after having an hour Zoom call with the person who's going to do it with them talking through it some, they then go write those things and then they engage with that person. It's always someone in product. We don't pull our engineering team in to do it. But they'll ask a follow-up question on the issue and then let them rewrite something in the issue or they'll ask them a question maybe that causes them to define something better. And I personally when I was interviewing thought this is a weird step, I'm coming in as a director at the company and then I finished it and it was like, "This is the best experience I think I've had. This has the standard interview process."

Lenny Rachitsky (00:46:38):
Wow.

David DeSanto (00:46:39):
And so that all ties together as that first thing. The second thing I tell everyone is don't wait. If you're concerned or learning something is going off the rails or you just want to know something's on track, don't wait until your next check-in point. A lot of the teams here do a once a week stand up, just ask a question on that issue or on the merge request or send a Slack message right away. The last thing you want to do is have a 24 hour, 48, 72 hour cycle go by and a developer or your engineering manager is stuck or they've asked you a question and now you're leaving them hanging and not getting the answer they need. And that's where, to your point, used to block up to a cubicle, taps one on the shoulder and be like, "Hey, what's going on?" And now it's got to do that digitally and that is reach out on the communication platform. We use Slack. It's like reach out on Slack or comment on the GitLab issue or merge request.

Lenny Rachitsky (00:47:36):
For this to work, the values again come up, where you assume good intent, you be kind people. Because I think oftentimes at companies at PM, checking in often feels like, "God damn, leave me alone, I just want to work on this thing. You just don't trust that I know what I'm doing." But I think with these values that helps avoid that, I imagine?

David DeSanto (00:47:54):
It does. And I think it also feeds back into those remote work items as well that it's actually good for you to over-communicate. It's actually good for you to focus on, is the outcome happening? You may end up in a situation where the outcome felt like it was really big, but three days into your one-month-long iteration, which we have here, all of a sudden you realize this can be knocked down a week, right? Well, now don't just wait, reach back out and say like, "Hey, this is done. What's the next thing?"

Lenny Rachitsky (00:48:25):
Awesome. You mentioned Slack is a tool you use. What other tools do you find really interesting that people may not be thinking about for working successfully in a remote environment?

David DeSanto (00:48:35):
I'm going to be biased here and say GitLab as a product, we call it dog fooding, but we use it for everything we do. And that's become key because it makes sure that the product shipping is going to work for our customer and our end user. But our policy here is like, "Hey, if you have the idea, open an issue and then tag your team." And then that issue becomes that single source of truth, then we can then turn that into an Epic or if it's going to become work for the engineering team, it can be converted into one of those types of issues. And we do it that way. We also encourage people to use Zoom. If you have too many back and forth. So say Lenny, you ask me a question, I answer it and you go it up, I don't understand. You ask it a different way and then I answer it again. You're still confused, like practically reach out and get on Zoom because maybe it's just something in writing's not translating. And so between those three main communication tools, that's what we use. GitLab is very anti-email in a lot of ways. Obviously we use it for external communication, but internally it's on an issue. It's in Slack or it goes into the handbook. So if we've made a decision together, whatever you and I were going back and forth on, we think this is really important. We go update that part of the handbook or add a new handbook page or whatever needs to happen so everyone can benefit from it.

Lenny Rachitsky (00:49:53):
So when someone updates an issue, do they get pinged in Slack when typical go check it out, it's not like an email.

David DeSanto (00:49:58):
Yeah, it does. If you have your notifications set up, any comment on something that you created, we will give you a new notification. The notification shows up in your to-do list in GitLab, you can have it send you an email. I have it actually email me and it goes into a folder. Actually created, we use Google Workspace and if it's a, you've been mentioned to do, it goes into one or gets one GitLab or a Gmail label. If it's a, "Hey, this was an issue that you're following that there's been activity on," that goes into a different label, and that way I can quickly find the ones that I should be responding to.

Lenny Rachitsky (00:50:34):
Got it. You talked about this handbook workflow. So I was reading a bit about that. So basically the handbook is like, it's like essentially treat US Code people submit PR requests to change the handbook, which essentially is changing the way the company's operating. Can you just talk about that workflow? There's a piece of update the handbook before you make change.

David DeSanto (00:50:53):
Yeah. So we talked a little bit about single sources of truth earlier, and one of those is the handbook for us, it's how the company operates. And so if you're finding something that's inefficient in a workflow or you're finding something is unclear, you're encouraged even as part of your onboarding to open up a merge request and make it right. And we sometimes make jokes in the product division because when product managers are onboarding the handbook feels like the product and their three week of onboarding, they may end up opening a bunch of merge requests for things like, "I found this typo, I fixed it," or, "The sentence could have been worded better so I reworded it, now it makes more sense." But then there's also the bigger thing. So our product development life cycle and that workflow and the framework that supports it is all in the handbook and it's in the public handbook. And so what that allows people to do is understand exactly how we're going to operate for a milestone. That iteration again where, "Hey, what's expected three weeks before, two weeks before from you?" And then that allows some of those values we talked about earlier to come into effect because now you've also have your EM on the other side who also has something similar and knows when to expect something from you, when not to expect it from you. But then if there are bigger changes, we of course have processes for those that are defined. Great example is, if you're going to introduce a new category, which new part of the product, it requires my sign-off to do that, right? If you're going to change that product development framework that helps you prioritize, that's got to be approved by myself, the CTO, as well as a lot of our directs that are involved in making sure we're delivering efficiently. And so it can all be from a team perspective to a global wide that you can contribute to. What we have encouraged people to do is create their own mini versions of these things because I want to provide guidance, I don't want to give you direction. And what I mean by that is, here's how I'd like you to prioritize. Here are the important things to the company, but whether you make that one milestone is a 100% new features, the next one's a 100% bug fixes. As long as you're achieving the outcome that we've said, how you get there is your own decision and then those individual teams create their own version and references back to the bigger handbook.

Lenny Rachitsky (00:53:13):
Got it. One more tactical question about remote work. What's your time zones policy? How do you align time zones and get people talking and not bothering each other when they're asleep?

David DeSanto (00:53:23):
That is a good question. So we focus on asynchronous communication first, and so that means that key decisions that involve people who are in a time zone where the meeting's not occurring, that waits until they're back online because the directly responsible individual or DRI as we say here. We also focus on making sure the meetings that do happen are optional and are both recorded as we talked about at the beginning, but also have really good notes. And so that way someone who's in a different time zone can read that and consume that when they're online. Our goal is to make sure we're as inclusive as possible, and so that includes even leadership roles. Our leader of our product portfolio for our SaaS platforms, which are Gitlab.com and Gitlab dedicated, he lives in Germany, but he is a leader at GitLab and his product team is in the US. I think he's got someone in South America, people in Western Europe and so forth. And so that means that he may not be online when parts of his team are online, but if he's communicating asynchronously and giving clear outcomes and empowering the people who make the decision, it's okay that they may not have overlap. I had a leader in our team who was in Tel Aviv. At that point I still lived in the middle of the United States. We had a half hour overlap in our day, but she was always highly efficient as a leader and her team was also geographically dispersed and they were highly effective. And to give you the way I've looked at it, it means that you can empower the people around you so that you don't have to worry about those meetings that happen at weird times of the day for you. A good example, if I can't make it to a leader or a meeting that is more APAC time friendly, maybe that's where a lot of the team members are. I have leaders on the west coast of the United States who will take that call and they're empowered to do that. And so that's how we deal with it. We are in 60 countries or over 60 countries at this point. We've had to be very careful to be inclusive and that's what drives those things. Well, note-taking, recorded meetings, that asynchronous focus on communication.

Lenny Rachitsky (00:55:32):
I was just thinking that with all the recordings you've done, you could train an LLM to basically run your business at this point. I imagine engineers are thinking about that.

David DeSanto (00:55:41):
I don't think anyone's thinking of that yet, though maybe they are. They have actually focused on how do you make a version of David who's in every meeting and they're playing with some of the AI generated stuff, training it on videos that I did. So we have a lot of fun at GitLab, but we also accomplish a lot too, is the takeaway from that.

Lenny Rachitsky (00:55:58):
Before I move on to a different topic, in terms of transparency or remote work, is there anything else that you think would be worth sharing or giving people advice on?

David DeSanto (00:56:06):
The best summary of the conversation is make sure you're focused on communication, being clear, setting the clear steps, like a framework for how to operate and be uncomfortable with the transparency to make sure people can follow along. And if you're doing those things right, remote is actually really great. I can't tell you how I feel today in a measurement that's not just like I'm really happy about it, but I just felt like other places I've worked where we had to hire two in office, it really limited the candidate pool you could have. And now being all remote, we can hire anywhere for the most part and find the best person for the role, and that's allowed people to have the life they want. I don't live in the Bay Area anymore and I think it's phenomenal. Your family and friends that I grew up with and I can still work that tech job and that's not just true for me, that's true for the gentleman I mentioned who's in Germany. We had an employee who was in Israel in the leadership team. We have PMs, UX, designers, technical writers. There are two searches all over. And that's not just true for product, it's true for every division at GitLab.

Lenny Rachitsky (00:57:19):
So I asked a previous guest who worked with you, Hila Qu, who was head of growth, I think at GitLab for a couple years, and I asked her what to ask you and asked generally about GitLab, and she said that GitLab is really good at this breadth over depth strategy of building product, and that's been the key to success so far. Can you just talk about that and why that's been important?

David DeSanto (00:57:41):
Yeah, so I did. I love Hila by the way. I worked with her for about, I'd say it was a little over two years, I think the time she was here, still talk to her occasionally over LinkedIn Messenger. Someone asked me, LinkedIn was dead by the way. I think it's how I stayed in touch with former colleagues and playing things out.

Lenny Rachitsky (00:57:56):
LinkedIn is killing it. I think they're on the way upswing. They're killing it right now.

David DeSanto (00:58:00):
I think they are. I think that's a whole nother podcast on why that is. But let's leave that., So Hila is right. So when she started in 2019, a couple months after me, we were very much focused on a breadth over depth. And that was so we could build out what is the DevSecOps platform. The only way that we could truly help people from a platform strategy was to be touching the different parts of the DevSecOps lifecycle or the SDLC, depending on how you look at it. Now, last year we made the conscious decision to start to pivot to depth over breadth. And that's because we have a very broad platform today. We are touching everything from business continuity planning and OKRs to enterprise agile planning and team planning to coding, deploying, securing, monitoring, the entire SDLC. And we now know there's key areas where we need to be really deep to help companies accelerate delivering software. And so in those key areas, they are source code management. The things around that like code review, ID experience, remote development, CICD, security and governance, planning and AI, we know of those are really deep. The things that aren't as deep around them, we'll get that a rising tide of solve boats effect. And so we've pivoted in those queries now be depth over breadth.

Lenny Rachitsky (00:59:20):
That's awesome. It's interesting. So basically, to create a wedge and gain traction, sounds like initially let's just do a lot of things but not be the best. And now that you're doing great and have all these products, the strategy has shifted to going deep. This is a question a lot of founders always face. Should we go wide? Should we go deep? I know you weren't there at the beginning, but just I guess do you have any thoughts or insights from when it makes sense to go wide versus when it makes sense to focus? Because usually the advice is just do one thing really great and that's the only way to win. And it sounds like clearly this is an opposite approach here.

David DeSanto (00:59:55):
And for those who aren't as familiar with GitLab as I know you are, we are the leader in our space. We are the DevSecOps platform. Not just us calling that, but user reviews, analysts like Gardner and Forrester are calling that out. And so what for us it was that I think when you're going really wide, you're trying to find your niche and what you're going to be really good at and what you can differentiate on. And for us what that was is where are the key areas that we can truly help someone accelerate delivering software. And over the course of those years, you're right, we were still in a fast growth period when I started and I was part of that breadth first when I started in 2019. But we found those key areas that we know if they are truly deep, they bridge to the other area that's deep and maybe some of those areas don't have to be as deep as the things around them. And so good example is we started adding ModelOps functionality to GitLab in 2020. We focused heavily on adding depth to MLOps, which is just one of the three pillars of that. And we know that DataOps will probably be needed at some point, but if we have a nice integration with DataOps platforms, you can actually do all your MLOps work in GitLab and be successful at it with a lightweight connector or component that's there. And so that's what we've done, is we've started really investing deep in those key areas knowing that it's going to help those areas that we aren't investing necessarily as much in be still good enough. And touch on what you were touching on earlier about the getting to that good enough level.

Lenny Rachitsky (01:01:31):
What's interesting is my last interview that I did was with the co-founder of HubSpot, Dharmesh, and they had the exact same strategy, breadth over depth. Also, one of their core values is transparency. They share all of their financials with everyone, salespeople, everyone, they see everything. So it's so interesting that this companies are very different and have very different markets, but there's two really similar elements here and I've worked out for both I guess. Does that bring up anything? I don't know how much you know about HubSpot.

David DeSanto (01:02:00):
I know the company and know some people who worked with me in the past that have gone there. I think what you're touching on is that there's some product frameworks that are universal. I occasionally will have founders reach out and ask the question, when do I make that pivot? And it's really like, have you found your fit in market and have you done the whole, you'll use Jeffrey Moore's book, the Crossing The Chasm. Have you found that? And if you have, now to put all of your wood behind that arrow to use a saying, right? And then you're able to get that differentiation in that market presence. And we go back to breath over depth when we're looking at new investments. So it's not like it's left GitLab, it's currently part of our AI strategy that we're finding the spots for depth psychology makes a lot of sense. But we also know that if those five things I shared with you are leading and we see them as leading in the industry, it's going to give us the ability to do more of that breath over depth as we try to expand our SAM or try to go after a new market.

Lenny Rachitsky (01:03:06):
What's interesting with Dharmesh's approach, I'll share briefly, is their internal metric was, "If we're the top three product in any of the categories, we're doing too much. We're investing too much in these products. We don't want to be the top three in any of these yet. We just want to be fine because holistically it's going to be great." But just I want to move on from this topic, but just it's interesting, the approach you shared for GitLab or why going wide made sense was explore opportunities and then go big when you find something that works. HubSpot's strategy was our customers need all the problem they have includes needs, all of these many things. And so to solve their actual problem, it turns out we need to build a lot of things the way it is. And I imagine that was a part of GitLab's need to?

David DeSanto (01:03:51):
Yeah, I'm sure as we grew, I joined 2019, company started years before that, and I've just seen the maturity of the company as a whole and the growth and the need to focus on going deep in some really core areas. But like I said, we still go back to that same approach that they have. It just depends on what we're talking about and why we would make that decision.

Lenny Rachitsky (01:04:12):
Cool. Okay, just a couple more questions. I know you guys are doing some cool stuff with AI. Let's talk about that. What's going on with AI and GitLab?

David DeSanto (01:04:19):
I would say we've taken a very unique approach to AI as part of software development. And the reason why we did that is that GitLab has a very unique position. We are a true DevSecOps platform. A lot of our competitors that people talk about are like a developer platform or developer experience type tool. And we know that if 25% of the SDLC is actually creating code, 75% is not, and we want to help all those people around the developer be it successful. And to do that, we set ourselves like three core tenets or principles for AI a couple of years ago. The first one was AI across the entire software development life cycle, we want to help product managers, QA teams, ops teams, security teams also benefit from AI. If you make your developer a hundred times more effective, it just means probably everything around them is going to break. And so to make them more effective, you've got to help everyone. The next was we wanted to be both transparent, which fits into our conversation earlier and be focused on privacy with AI. And that means that we tell you what models we're using, we're source available so you can see how we're using them. We tell you how they're trained. And the privacy part is we don't use your intellectual products for training and fine-tuning models. Our models are trained on data that is not yours, which means that you don't have more safety in using that. I think other companies have shown why that's important with leaks of customer data and we want to avoid that. I think the thing that's interesting, as a source available open core company, we're actually trusted by more than 50% of the Fortune 100. So if more than 50% of those top companies trust GitLab to secure their intellectual property, we had to do that with AI as well. And then the last one was AI efficiencies. We wanted to make it so there was a boost efficiency. GitLab ultimate, our top tier has a 7X boost on productivity. As from our customers doing a data analysis of their improvements, we want to take that to 10X as part of it. And so we think AI can give us that last little bit of a burst. Now I did mention a minute ago and me, I'll stop there to see if you have questions on those. And then I just want to talk a little about where we're going with AI because I think it's pretty exciting.

Lenny Rachitsky (01:06:38):
I guess the only question is just for other companies, other product leaders thinking about integrating AI, working with AI, any tips or lessons you can share that might be helpful on their journey?

David DeSanto (01:06:49):
What I would say is we spend, and this is really the third tenet, is finding the right model for the right use case. And good, I pointed out your question, reminded me of it. What sometimes people will do is they go, "Oh, there's this really popular large language model," whether that's a commercial or open source, and then they make everything fit into it. And what you end up doing is actually reducing the quality that someone can experience with that feature that's leveraged by AI. And so I encourage people to find the right model for the use case. We have around 16 models we use today to make GitLab have its AI suite, which is called GitLab Duo. And we've done that to say like, "Hey, this one's really good at explaining and resolving vulnerabilities. We're going to use that for that use case. This one's better at summarizing conversations and plan. Let's use that." And of course, code creation is also an area where if you're using the same model for inline code completion as you are for code generation, which is generating blocks of code, you're going to have a much different user experience. The things that generate blocks of code like functions, those actually take a while to run. They take seconds, sometimes 20, 30 seconds to fully respond. If you're just asking for the next couple lines to be completed, you're not going to wait that long. And so you've got to have something that can handle that as well. And so we've done that and I encourage everyone else to do that. If you go to the GitLab Docs website, you can select GitLab Duo and you'll see all the models we're using and you can start to understand as you learn about those models, you start to see why we chose them. And it actually has allowed us to get closer and closer to that 10X that we're wanting to get our customers to.

Lenny Rachitsky (01:08:27):
I'm pulling up that page. But when you talk about models, are you talking about open AIs, APIs for one and then Gemini for another, or is it like internal models you're building?

David DeSanto (01:08:36):
It's both GitLab created, open source and commercial. Today we've partnered with both Google and Anthropic and those are where the commercial models come from.

Lenny Rachitsky (01:08:46):
Got it, got it. Cool.

David DeSanto (01:08:48):
And then we actually acquired a company at the beginning of 2021 or 2022 named UnReview, and we have those models. Those are the ones that would be GitLab proprietary. And then we do use Open source as well. We're actually looking at how we can leverage open source more and contribute back there. We have a really awesome AI model validation team that are a bunch of AI researchers that have studied things like ethical AI and AI at scale, and that's allowing us to select the right model.

Lenny Rachitsky (01:09:19):
Cool. I imagine part of this is because GitHub, your competitors owned by Microsoft and OpenAI and you try to avoid that whole area, as I'm guessing is a part of this thought process.

David DeSanto (01:09:29):
Well, it is also about meeting those tenants, right? And so our partners at their commercial, they need to meet that same requirement and that same vision. And both Google, as in Google Cloud and Anthropic, were able to meet the privacy requirements we had, and those are really important to us. And so not every company that we could partner with could do that, and so we had to be very careful as to who we partnered with. And so there's nothing about the companies we're not partnered with. Maybe we just haven't gone to that point yet. But that's part of being a partner is you have to meet those same values for lack of a better, to put it that we have base of our customer base, especially being trusted by more than 50% of the Fortune 100.

Lenny Rachitsky (01:10:13):
Makes sense. Okay. Going a totally different direction, Hila also said that you're a leader with a great sense of humor and you often use your humor to navigate very high stakes conversations and executive negotiations. And I think a lot of people would love to have the skill. Do you have any advice or lessons other than just being David and being who you are, I guess any lessons for leveraging the skill, building the skill, how you apply it?

David DeSanto (01:10:39):
I'll take the compliment from Hila. What I learned early in my career is that tension, especially very high, very tension driven conversations can really kill productivity, kill morale. And that I found that if I can deflate that a little bit and re-add some, I don't want to say humanity to the conversation, but really disarm the topic, that people are able to move forward. And I think that's what she's talking about. I will say that it probably is partially David being David to a degree. Maybe I'm the class clown experience of my elementary and high school experience and harnessing it for good now. But I think people can also do that. And leaders who have seen me do that, like Hila have learned that there's ways to do that if you can read the room and the nuance and know whether or not it's okay to try to add a little bit of levity, but I consider it a value part of my tool belt now, like a tool in my tool belt and I'm glad she appreciates it. Not every joke lands, which I'm sure you're not surprised by that, right? But yeah, I think it's been good to help keep people moving forward.

Lenny Rachitsky (01:11:52):
Love it. David, is there anything else you wanted to share or touch on or leave listeners with before we get to our very exciting lightning round?

David DeSanto (01:12:00):
The big thing I just like to let people know, if you're not familiar with GitLab or you haven't heard of GitLab in a couple of years, please go check out our website. We do everything across the software development lifecycle. When I started in 2019, I was hired at compliance and security to DevOps, which has made us a DevSecOps platform. And now we've gone from not just source code management and code review or CICD, but true security and governance. That includes things like our remote development offering where now you can even get developers up and running in minutes on a software project. Our enterprise planning capabilities, and of course GitLab Duo. We've heard from customers, they've seen efficiency boosts of 50% and above by leveraging GitLab Duo. And I would say if you've not heard from us in a while or aren't as familiar, please just check that out because we are truly unique in the space and it's something I take a lot of pride in. People said, no one's going to want a platform. They want a bunch of point solutions and customers end up with 75 tools to try to deliver software and they adopt GitLab and all of a sudden they realize how much more effective they can be in collaboration. And even that transparency stuff, we talked at the beginning.

Lenny Rachitsky (01:13:12):
I'm at the website and even then I'm like, I think it could do a better job telling me everything that you do. So just to quickly summarize so people know, what are the bullet points of all the products and solutions you guys offer real quick?

David DeSanto (01:13:24):
We do everything across the software development lifecycle. Some areas are really strong. Those key areas are SCM, code review, what would be called the create stage in the tool chain. CICD. We're industry leading there as well. Security and compliance, so we can do application security scanning, we can do things like software bill and materials and traceability and all the things that go around compliance and governance. And then of course we also have monitoring, whether that is value stream management and analytics. We can now do product analytics. So you can have GitLab embed telemetry and then see how that app is being used. And we are currently working on expanding into observability and service management. But it is truly an amazing experience if you start with just an idea in our planning functionality, again, been awarded a leading enterprise digital planning solution, and then take that from idea all the way to running in production and then learn from that and bring it back into the life cycle. But I'll take your feedback line back to marketing and say, I was just on an amazing podcast, met a great guy, hopefully get to talk again in the future. And he said, I can't come back until the website's better, so can you please just make it a little bit clearer?

Lenny Rachitsky (01:14:42):
Yeah, make the website clearer, software faster. That doesn't tell me what I need to know. I like this list you gave me. Okay, amazing. We're solving all the Gitlab's problems right here.

David DeSanto (01:14:52):
There we go.

Lenny Rachitsky (01:14:54):
With that, we've reached our very exciting lightning ground. Are you ready?

David DeSanto (01:14:58):
I am ready.

Lenny Rachitsky (01:14:59):
What are two or three books that you've recommended most to other people?

David DeSanto (01:15:03):
The two that I probably recommend the most are Crossing The Chasm by Jeffrey Moore. The current edition still has some things that are a little bit older now as examples, but the core of it is still very, very amazing. The other one is Essentialism, and that is really about saying no to the right things and finding the thing that you really need to do to get the job done. And then not a book, but Jeffrey Moore created this. There's the critical core context framework, and if you've read both of those books, it really helps you frame in what is the critical part for your business, what is the core of the expectation and what are the things that you can say no to with the little bout of risks? So those things together, I think are really powerful.

Lenny Rachitsky (01:15:44):
Does he talk about that in Zone To Win or is that just something independent of his books?

David DeSanto (01:15:48):
I think it was a class he created and it turned into a chapter two in one of his books. I don't remember which book it's in though.

Lenny Rachitsky (01:15:56):
Super cool. That'll work. Next question. Favorite recent movie or TV show you really enjoyed?

David DeSanto (01:16:01):
The most recent TV show I really liked, The Devil's Hour. It's a BBC show. If you've not seen it and you like Sci-fi crossed with, I don't know, call it a mystery, criminal type show. It's really, really good. Movie wise, it's an older movie. My wife just watched the Glass Onion, really liked it. And then there might be a little bit of a Swiftie in me, and we watched The Eras Tour when it came available to watch and also was phenomenal. I can't believe three and a half hours went by as quickly as it did.

Lenny Rachitsky (01:16:34):
I also watched it and enjoyed it. Do you have a favorite interview question you'd like to ask candidates that you're hiring?

David DeSanto (01:16:40):
Yeah, so I won't say there's a specific question. It's so much a method. So I really like the star method for asking questions. If people aren't familiar with it, Google it. It's really powerful. And then how I then apply it to be my favorite question, depending if it's PM or it's someone in engineering or another department is give them a scenario where there's a little bit of conflict or tension and having them work through that as an example. I think those really give you a sense as to how people can problem solve.

Lenny Rachitsky (01:17:09):
Do you have a favorite product you've recently discovered that you really love?

David DeSanto (01:17:12):
Yeah, so this is going to be a sad moment for me. My favorite new product is actually going away. Artifact News.

Lenny Rachitsky (01:17:19):
I love Artifacts. Yeah.

David DeSanto (01:17:21):
I think it's actually hit the point where it's hit its end of life, but it was revolutionary for news. I thought it was fantastic. The things I use that are not the app that just went away that just a little bit bad about, I've really gotten a love for Superhuman, for email. It's really allowed me to make, we're a Google Workspace customer more powerful. And most recently, I just started using the Arc browser from the browser company and I think it's fantastic. I like how it organizes everything and archives tabs that they've been inactive for too long and all these things that I think just took me from a single Chrome window to like five windows each with a hundred tabs and has made me more effective.

Lenny Rachitsky (01:18:05):
Awesome. Also, a huge fan of Arc. The Josh Miller was on the podcast talking about how they operate and Superhuman is a sponsor of the podcast. So I love all your choices. Do you have a favorite life motto that you like to come back to or share with people that you find useful in work and life?

David DeSanto (01:18:20):
I actually have two or three. I'll say them quickly for everyone, but the first is as a leader, my first one is, "Your team's accomplishments are theirs, but their failures and misses are yours." And I, early on in my career would've loved to feel like sometimes my work wasn't just then praises for my manager. And as now a leader of a very large team at GitLab, it's been important. The one that my team laughs at that I say a lot is as a general motto, I'll go, "Just make it work." And people who are listening to your podcast might realize that's a Tim Gunn saying from Project Runway. And it was my way of taking on the work the problem statement and making it a little bit more like, "Okay, this is the thing you have to figure out, make it work. What does that mean for you?" And so it also lets me throw in pop culture too. And the last one, and I'll say I came up with this when I was back as an engineering director was, "It's just software so anything's possible." A lot of times someone will say, "Well, I can't really do that." It's like, "Well, but it is just software. It hasn't been done yet, but it's doable."

Lenny Rachitsky (01:19:32):
David, this is so fascinating. The culture at GitLab is fascinating. You're fascinating. Thank you for making time and sharing all these stories and insights. Two fun questions. Where can folks find you online if they want to reach out and learn more? And how can listeners be useful to you?

David DeSanto (01:19:44):
If you want to follow along with GitLab, we're @GitLab on basically every social, so go to any social media, you can find us. For me personally, I'm D. DeSanto on LinkedIn. You just search for David DeSanto, I should come up. I'm David_DeSanto on X. And as I mentioned earlier, I am DavidTheBeard on Threads. I'm also trying to make Blue Sky a thing for me, so if you want to catch me there, I'm just D. DeSanto on Blue Sky. And then how listeners can really help. There's really two things. One, please share feedback with GitLab, with my team. You can go and comment on our issues or ethics, our tasks, it's all public. So vote things up, give us feedback, that's always very helpful. Just go to GitLab.com and you can see our code base. And then if you are someone who wants to contribute, please open up a merge request, improve the handbook. Companies fork that handbook, and then use it for themselves as well. So you're not just helping GitLab, you're helping everyone. As well as maybe contribute to the code. It can be as simple as fixing a small bug to adding a new feature. Some of our favorite features are ones that others have contributed outside of GitLab.

Lenny Rachitsky (01:20:50):
Awesome. Well, David, again, thank you so much for coming and sharing. Now I'm going to go watch this meeting you're in later on YouTube. Anyway, thanks for coming and thank you.

David DeSanto (01:21:02):
Yeah, thanks for having me, Lenny. And love the conversation. Let me know whenever, I'll come back.

Lenny Rachitsky (01:21:06):
Amazing. Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at Lenny'sPodcast.com. See you in the next episode.
