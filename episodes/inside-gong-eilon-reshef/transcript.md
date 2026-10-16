---
guest: "Eilon Reshef"
title: "Inside Gong: How teams work with design partners, their pod structure, autonomy, trust, and more | Eilon Reshef (co-founder and CPO)"
publish_date: "2025-01-02"
source: "https://www.lennysnewsletter.com/p/inside-gong-eilon-reshef"
slug: "inside-gong-eilon-reshef"
archive_id: 153430776
topic: "Inside Gong: How teams work with design partners, their pod structure, autonomy, trust, and more"
description: "Gong CPO Eilon Reshef on their unique team pod structure, how pods work with design partners, his spiral method for mastering complex topics, and more"
summary: "Gong CPO Eilon Reshef on their unique team pod structure, how pods work with design partners, his spiral method for mastering complex topics, and more"
youtube_url: "https://www.youtube.com/watch?v=HL7PS0fy1Ho"
video_id: "HL7PS0fy1Ho"
duration_seconds: 3402.0571
duration: "00:56:42"
channel: "Lenny's Podcast"
transcript_source: "substack-transcription"
---

# Inside Gong: How teams work with design partners, their pod structure, autonomy, trust, and more | Eilon Reshef (co-founder and CPO)

## Transcript

Lenny Rachitsky (00:00:00):
I want to start with talking about your pod model, which is a really unique way of building and organizing your product teams.

Eilon Reshef (00:00:06):
That was probably 2016, we're trying to figure out how does the operating model look like for product and engineering. The first bunch of people we had was essentially a pod, it was one product manager, a user experience designer, backend engineers, a couple of front-end engineers, but at some stage we're starting to scale, we are kind of contemplating do we go the traditional, the old school of front-end engineers, backend engineers, and then we said let's try to replicate what we have.

Lenny Rachitsky (00:00:28):
Let's talk about how these pods work with design partners, from what I've heard, it's very unlike how any other company works.

Eilon Reshef (00:00:34):
We just took the pod concept to an extreme, where every pod is working with sometimes a dozen design partners, sometimes two dozen design partners.

Lenny Rachitsky (00:00:41):
And this feels like a cheap code of how to build new product lines. What are the percentage of success rate you have with new product?

Eilon Reshef (00:00:49):
I would say very close to 100% of the features we build end up being used by a significant number of people.

Lenny Rachitsky (00:00:54):
Does it feel crazy for companies not to operate this way?

Eilon Reshef (00:00:56):
I wouldn't go back. I hate terms such as risks because that's a very ambiguous term, but just the risk of building something you're not going to know if it's going to get used.

Lenny Rachitsky (00:01:04):
So, when I ask people at Gong what to ask you, the most often term that came up is autonomy and trust.

Eilon Reshef (00:01:09):
It's a very selfish thing, it's a very personal thing, I just think...

Lenny Rachitsky (00:01:16):
Today my guest is Eilon Reshef. Eilon is co-founder and chief product officer at Gong, he was also a long-time chief technology officer at Gong. As I share at the top of our conversation, it feels like basically every company that has a sales team uses Gong, and it's really rare to build a product that is so ubiquitous and so loved across the tech ecosystem. In our conversation, Eilon shares some of the secrets of what makes Gong so consistently successful, including how their product teams work with six to 12 design partners on every new product and feature that they invest in, how he creates a culture of autonomy and trust, why and also how he optimizes for making decisions quickly, even large one-way door decisions, what he and his team have learned about building AI-based products, since they've been building AI-based products longer than most other companies, and so much more. If you're building a B2B SaaS company or product, you will learn a lot from this conversation. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube, it's the best way to avoid missing feature episodes and it helps the podcast tremendously. With that, I bring you Eilon Reshef. This episode is brought to you by WorkOS. If you're building a SaaS app, at some point your customers will start asking for enterprise features like SAML authentication and SCIM provisioning. That's where WorkOS comes in, making it fast and painless to add enterprise features to your app. Their APIs are easy to understand so that you can ship quickly and get back to building other features. Today, hundreds of companies are already powered by WorkOS, including ones you probably know, like Vercel, Webflow and Loom. WorkOS also recently acquired Warrant, the fine-grained authorization service. Warrant's product is based on a groundbreaking authorization system called Zanzibar, which was originally designed for Google, to power Google Docs and YouTube. This enables fast authorization checks at enormous scale while maintaining a flexible model that can be adapted to even the most complex use cases. If you're currently looking to build role-based access control or other enterprise features, like single sign-on, SCIM, or user management, you should consider WorkOS. It's a drop-in replacement for Auth0, and supports up to 1 million monthly active users for free. Check it out at workos.com to learn more. That's workos.com Hey, it's Lenny, if you want to boost your clarity and confidence, I want to recommend a podcast called Think Fast, Talk Smart. One of the most essential ingredients to success in business and in life is effective communication. Every Tuesday, host and Stanford graduate school of business lecturer, Matt Abrahams sits down with experts to discuss the best tips and techniques that enhance your professional development. Hone your small talk, influence, presentation skills, and so much more on Think Fast, Talk Smart. So, what are you waiting for? listen every Tuesday, wherever you get your podcast and find additional content to level up your communication at fastersmarter.io. Eilon, thank you so much for being here, welcome to the podcast.

Eilon Reshef (00:04:27):
Thank you for having me.

Lenny Rachitsky (00:04:28):
So, it feels like on this podcast every guest that I've had mentions Gong as a product they use, it feels like it's just like in the ether of tech companies these days. Also, I've heard so many times how unique it is that you all operate, how you all build your product teams and operate, which is, I especially love hearing on this podcast just different ways of operating, so I'm really excited to dig into this, to hear about the journey and things you've learned along the way of building Gong, and essentially building something that is so ubiquitous and so loved, which is very rare. I want to start with talking about your pod model, which is a really unique way of building and organizing your product teams, and in particular how you work with design partners. But let's start with the pod model, can you just talk about what this pod model is and how you organize your product teams?

Eilon Reshef (00:05:13):
Sure. And when we started the pod model, that was probably 2016 before it became more popular, I think that might've been even before the Marty Cagan set of books, I don't remember exactly. But at some stage we're starting to scale, scaling is maybe from 50 people to 60 people, in the whole company or whatever, and we're trying to figure out how does the operating model look like for a product and engineering. And the first bunch of people we had was essentially a pod, it was one product manager, yours truly, a user experience designer, a couple of maybe backend engineers, a couple of front-end engineers and whatnot. And we were kind of contemplating do we go the traditional, the old school of front-end engineers, backend engineers or however it is? And then we said let's try to replicate what we have. So, what we essentially did is really replicated that. So, up until now we have this pod structure, product manager UX, fractional writing, fractional analyst, and then a team leader from an engineering standpoint, five to I'd say seven engineers, they get an agenda, think like we launched a forecast product, that was a pod working on that, and then they get to be pretty autonomous in identifying how to solve the problems, and also working with enough customers so I can go to sleep knowing that they're not hallucinating is the term that everybody uses now in different contexts, but going in a very reasonable direction.

Lenny Rachitsky (00:06:35):
So, I want to talk about the autonomy piece, so that's a really important point, but before we get there, let's talk about how these pods work with design partners. From what I've heard, it's very unlike how any other company works, and I think it's something a lot of people can learn from. So, talk about the scale of how these pods work with design partners.

Eilon Reshef (00:06:51):
So, I think we just took the pod concept to an extreme, where every pod is working with sometimes a dozen design partners, sometimes two dozen design partners, maybe sometimes five, if it's a very niche or fringe capability, and they work with them hand in hand. So, an interesting story, the same forecast product I just mentioned, the product manager comes to me one day and he's like, hey, I just going to play with a design partner on the product. And I kind of know what's going on and I know it's not built yet, so I asked the product manager, but we don't have that working. So, he said, no, no we don't, but I showed him the half built stuff, I asked him to hit save, he hit save, and got an error message. And I told him, let's meet again in a week, and that save button was going to work. So, it's very extreme in terms of working hand in hand with the customer. Customers appreciate it, I later got feedback that they appreciate how the thing was making progress according to their feedback, not what they said, but interpreting what they said, digesting it, and building something that makes sense. So, every pod has this set of design partners.

Lenny Rachitsky (00:07:52):
So, these pods essentially cross-functional product teams, each one has... Do you organize it around an outcome? How do you describe what each pod is responsible for? Is it like move this metric, or build this product, or something else?

Eilon Reshef (00:08:04):
We tend to be less metric-driven maybe than your average, especially B2C, but even other maybe B2B companies. Usually it's more around some sort of a job to be done, in our case it could be sales engagement, how do you prospect? Or conversation intelligence, how do you create a summary? How do you make it easier for people to remove drudgery and consume information fast? Once you get this agenda, you pretty much have a lot of, you mentioned autonomy, a lot of control over how you progress. Ideally design partners guide you, not me.

Lenny Rachitsky (00:08:35):
Awesome. Okay. So, it's like, here's the outcome we want this pod to achieve, they have autonomy to work with design partners to design this new product. So, maybe let's stay on this example of this forecasting tool, can you just briefly describe what this tool, what it gives you, what it does?

Eilon Reshef (00:08:49):
Yeah, it's a product we launched a couple of years ago and it helps organization forecast where they land in terms of the sales organization. So, every sales organization, B2B sales organization, has a bottoms up forecast process. People submit numbers, people override that, AI helps you, in our case, AI helps you predict the right number, usually there's an analytics component on top of it, it helps you assess it at scale. So, that's the product itself.

Lenny Rachitsky (00:09:14):
Awesome. So, you created this pod, here, build this forecast product, make it successful, how do they find these design partners? Is it reach into existing customer base and figure out who would be most interested in this?

Eilon Reshef (00:09:24):
Usually it's existing customers, very, very rarely it would be a non-existing customers, but customers with some stage expressed interest in this capability. Not to over give a plug to Gong, but of course we can listen, all of our conversations are recorded, so I can always look up our conversation database and which customers express a need for X, Y and Z, you can very easily reach out to them. One of the maybe unique things we've done, at some stage it just became, I think we got like 25 pods right now, maybe 30, it depends what you call a pod. But it's a lot of effort, like this whole management, at some stage I borrowed an idea that comes from talent acquisition, and in talent acquisition recruiting there is a person called recruiting coordinator... If you do that scale, which we had done over the years. And that person, all they do is just set up the meetings for the recruiter, who then sets up the meeting for the hiring manager. So, in our product team, there's one person who's basically a research coordinator, and she's responsible for reaching out and she basically talks with the PMs, like what's your target market, ICP, whatever you want to call that, give me some... What do you want to learn from them? She reaches us, we have a micro CRM for that, and then sets up the meeting, and the PM comes in, they have already a meeting in their calendar.

Lenny Rachitsky (00:10:41):
And these are the people at these companies that are going to be their design partners?

Eilon Reshef (00:10:45):
Exactly. So, I might say, hey, what I want to speak is with head of rev ops at midsize companies, or IC seller at an enterprise company, and then she can, of course, sift through our customer base, slice and dice it, run a micro email campaign, and get those to come in.

Lenny Rachitsky (00:11:01):
I love that detail, because as you said, coordinating 12 companies and people at these companies and timing is really stressful and complicated and could suck the PMs life up. So, that's really helpful. It's interesting, there are some companies where product teams aren't even allowed to talk to customers, salespeople are like, no, don't mess with these people, customer success is like no, we got this. You were like the complete opposite, each pod is working directly with, say, a dozen customers helping build a new product for them.

Eilon Reshef (00:11:31):
Exactly. And in the early days we didn't even tightly coordinate with customer success. Nowadays, we do it much better because there's always going to be, this customers frustrated about something, or in a negotiation about something, that's probably not the right time to ask them about to be a design partner. So, we double check, but it's not like a process where we have to get signed off by three customer success managers to talk with a customer.

Lenny Rachitsky (00:11:54):
That makes sense. Yeah, you don't want to surprise people and mess up relationships. So, is there any structure to the design partner process or is it just teams have these people available and they talk with them when they want? Or is there more structure to how to effectively build the product with design partners?

Eilon Reshef (00:12:10):
It depends on the context. So, when you build a new product, it's a more linear path. Ideally you want it to be launched sometime. Ideally you want to measure some progress, so usually what we've done in this case is some sort of a weekly meeting where we show them progress, and sometimes bi-weekly depending on our own cadence. And some other capabilities that we build might be more, I want to say free form, maybe it's an enhancement, maybe it's tweaked, maybe it's an extension of the... I'll give an example, one of the things we do right now is we let customers ask a question about an account. So, coming to Gong, like what's new with Cisco? If Cisco is a customer. And at some stage you do it, we're doing it in all languages. So, you want to recruit a specific set of design partners who are non-English speakers. So, that doesn't have a strict timeline, you want to get enough of them so you see the thing works, gets your reasonable quality results. You're not going to get to all languages on the one hand, but at the same time you don't have just Spanish. So, that might be less structures, maybe it's a couple of minutes with each one and then we move on, you launch the feature, and you move to the next "project or feature."

Lenny Rachitsky (00:13:13):
So, one thing that people might be thinking as they hear this is, all these customers are telling you, here's what I need to be to use this forecasting tool, for example, and as a PM it's always this balance of doing what customers ask you to do versus, oh, we have this vision and here's how we keep it simple. What guidance do you give your teams for what to do with this feedback, essentially?

Eilon Reshef (00:13:34):
Yeah, I think this is core skill that I expect PMs to have around this, this is exactly your job, try to figure out what request is must-have versus not must-have. We typically, they ask the customer, what do you have right now? How happy are you between zero and 10? Or whatever. So, if you're at the six, we want to get you to an eight or a nine, so that's maybe a high level principle, but at the same time I expect them to say, hey, this is a unique... I didn't hear it from anybody else, maybe I'm going to practically reach out to more customers, but that might be a one customer thing. And we still do one customer things in different context. So, if we have a, I don't know, seven or eight figure deal, that they have one customization that they really, really need, and we know that they can't work without it, every enterprise facing company we're going to do that. But from a design partner perspective, it's the opposite, it's more like let's try to build something that works across our customer base versus for a specific customer.

Lenny Rachitsky (00:14:25):
Which is why a dozen is probably smarter than one or two or three.

Eilon Reshef (00:14:30):
Yeah, I think at some stage I guess you get seven or eight or nine at some stage, based on my experience, the request starts to converge. There might be one outlier, but generally you're going to hear the same things.

Lenny Rachitsky (00:14:40):
I imagine this approach is rooted in how you all started. We worked on a post back in the day on how you all got your first 10 customers, and I remember the story was you got, I think, 12 design partners when you first designed Gong, and then you told them, okay, we're going to start charging now, and 11 out of 12 are like, we will buy this now, please charge us, and we love it.

Eilon Reshef (00:14:59):
Exactly, exactly. So, in a way it's replicating this, but it was successful at the time, it was maybe 80% intention at a time and at some point you take the stuff that works and you make it 100% the attention.

Lenny Rachitsky (00:15:10):
What are the percentage of success rate you have with new products because you would think this approach is the best way to consistently build products people will end up buying and using. Is it like 100% of the time you end up building things that people will buy and use, is it something below that? What do you find?

Eilon Reshef (00:15:27):
I think it does increase significantly the utility of the products, I would say very close to 100% of the features we build end up being used by a significant number of people. We don't charge for all of them, for most of them we don't charge, which doesn't mean other things couldn't happen, maybe people use it, but the value is not huge. So, it's like yeah, design partner like it, but it ends up being applicable to a smaller fragment or segment of our customer base than what we had hoped. It may be they're not as willing to pay for it, although that's a little bit of a different process, like real product launch. It could be the quality is not good enough because we're focusing on, is it providing value, is it understandable versus did you find a bug when you used, I don't know, Safari, on this kind of computer. Because we're not building the design partner program to solve for this, maybe we should, but we are not doing it right now. But generally speaking, I would say better than that, more than 95% of the capabilities we build are being used in a very significant way.

Lenny Rachitsky (00:16:28):
Which I think is probably higher than most companies. And this feels like a cheat code of how to build new product lines, expand a product expansion, TAM expansion, like ways to add new ways to charge your existing customers, and it feels like a cheat code basically, just tell us what you need, we'll work with you and build it and we'll sell it to you and it'll be great.

Eilon Reshef (00:16:48):
Yeah, respectfully, yours truly, I do believe customers know much better than what they need, and then myself or my colleagues in the executive team, whoever else, it's you talk to a customer and they describe the pain. They might not know how to build it or what's the right way to implement it, but the pain should be there.

Lenny Rachitsky (00:17:06):
Coming back to something else you mentioned, this word autonomy. So, when I ask people a Gong what to ask you and what stands out about you to them as a product leader, the most often term that came up is autonomy and trust. How much autonomy you give teams, how much you trust teams to do the right thing. Can you talk about that way of working, where that came from, and why you think that is the way to operate?

Eilon Reshef (00:17:30):
It's very selfish thing, it's a very personal thing. So, I think even beyond trust, it's just, for me, it's selfish. I'll tell you why, I just think you get more from everybody if you let them be themselves, and do things in the way that they believe is the right way. Of course within limits, right? They're not going to develop, I don't know what it is, software in different business. But the story I always like to tell is, when my son was in primary school, which was a while back, one of the parents told me... And we had this picnic where all the parents and the kids were going to meet. And usually there's a list of ingredients that people need to bring in, to bring on a bottle of water, whatever the thing is. And what's usually happened, there's even people are joking about it, is people run to the list, because it's usually a physical list, and then... Or [inaudible 00:18:16] probably now it's already in Google sheets always. And people run to just mark the item that is as easy to get as possible. Like, a bottle of water, and then I'm done. And then, you always get the lowest common denominator because everybody brings the sort of, I don't want to even say cheapest, the easiest thing that you can bring to such a picnic, and this lady told me, here's a different method, just tell everybody bring your own thing. I'm like, are you crazy? People are just going to not bring anything, or whatever you want. Or people are going to bring the same thing. Multiple people are going to, I don't know, bake some pie, or do something. And she's like, no, that's not going to happen. So, I trusted her, that's maybe a trust word, but we tried it out, and what happened was really kind of fascinating. People were going out to the specialty stores and bringing special cheese... I'm based in Israel, so they were going to this hummus place, which is an Israeli thing. And just driving 30 miles to your favorite thing, people were baking and making stuff. So, we had literally a feast. And the funny thing, two things happened. Everybody was much, much happier, they were happier because of course they got better food. And also, most people, just their personality, they brought it to the tables, like I really like hummus, I don't like whatever the other thing I would have to bring. And we did it every year afterwards because we did this thing at least annually, and it will work every single time. So, if you take it to the software, you can't tell everybody just develop your own thing, but if you can guide them towards, hey, do the thing that... Give him more autonomy, essentially, bring yourself to the game, be yourself, don't try to put yourself in a box, I truly believe you're going to get much better results, short, and even more importantly, long-term, because it keeps people thinking, it keeps them being motivated, and they're like, how do I contribute in the way I think is the right way?

Lenny Rachitsky (00:19:58):
It reminds me, I'm looking for daycares for our son, he's almost 17 months now, and there's this Montessori approach to teaching kids, and it's a very similar approach, which is just let them... If they're ever busy with anything, don't even make eye contact, don't interrupt them, let them keep doing the thing, and let them choose what they want to work on.

Eilon Reshef (00:20:18):
Yeah, there's many, many of these education systems or principles that are along those lines. The person who told me that, I don't assume she's invented it, but we all err on the side of wanting more control. But I do the same thing with my kids. So I would never... I never installed any piece of software on my kids' devices. So, not firewall protection, I don't know, antivirus, error tag, nothing, because I'm like this is your problem, and if you want to protect yourself, it's your responsibility. So, this is autonomy. And there was one time where I had negotiated with my daughter, she was like, I told her I think you're using your computer too much, and we negotiated. She said, maybe an hour is enough, I told her maybe more. I think we agreed on a two-hour thing, and then she came to me three days in a row, could you please install the software on my machine so I can... Help me control my limits. And I love it when it's the other way around because now she's responsible, I'm helping her versus the other way around. So, absolutely, I take it in my personal life as well.

Lenny Rachitsky (00:21:19):
So, how does this look day-to-day at Gong on the product team, when someone hears, oh, you give them a lot of autonomy, what does that actually look like? Help people understand what that actually means.

Eilon Reshef (00:21:29):
It means that if you're working with design partners and you get an idea from the customer, it's your responsibility to decide are you going to do it? Are you going to talk to your manager, or to me? Now, I have, of course, group managers, but it's your responsibility. So, we're not going to "punish you" if you decided that you kind of took it an opinion from a customer and went ahead and did it, it's your responsibility to decide, do I know enough? Do I need more input? How up do I go? And that requires them to think, how confident am I in my decisions.

Lenny Rachitsky (00:22:06):
So, is the culture basically you give them feedback and advice and the teams can operate the way they want, they can build the features they think are important, work with design partners that they think are important?

Eilon Reshef (00:22:18):
Yes, and of course you are expected to solicit feedback. So, if you're going to build your own thing for six months and it's going to be... Well, we're going to review it along the way, of course. But we expect you to initiate a review. We have a weekly session where you can bring up your reviews, but it's not us forcing you to do it. You have to bring it, you have to solicit and you have to drive the process.

Lenny Rachitsky (00:22:39):
This episode is brought to you by Vanta. When it comes to ensuring your company has top-notch security practices, things get complicated fast. Now, you can assess risk, secure the trust of your customers, and automate compliance for SOC 2, ISO 20000-1, HIPAA, and more with a single platform, Vanta. Vanta's market leading trust management platform helps you continuously monitor compliance alongside reporting and tracking risks, plus you can save hours by completing security questionnaires with Vanta AI. Join thousands of global companies that use Vanta to automate evidence collection, unify risk management, and streamline security reviews. Get $1,000 off Vanta when you go to vanta.com/Lenny. That's V-A-N-T-A.com/Lenny. Is there an example of a product or a really important feature that came out of this way of working where a team just like, hey, you don't think this is a good idea, I'm just going to do it anyway?

Eilon Reshef (00:23:39):
I don't think it goes up to a whole product, it's kind of very hard to... Because you have resources to build a whole product. But I do think there is substantial features that came out of it. Even the AI fine-tuning example I gave you before, it's like something came up in a hackathon, and people were like, let's start to build it, let's incubate it, and then they move forward. Of course we had to give them resources at some stage, but it wasn't like a top down, let's do this, it was more like, hey, we're trying it out, hey, we need a couple of more resources, we're trying out more. And at some stage we realized it's super important and then we "funded it" completely.

Lenny Rachitsky (00:24:15):
So, when people listen to this, some product leaders might be thinking, oh, I want to work this way, I want to give my teams more freedom, more trust, what needs to be true in your org for this to work well, versus it become chaos?

Eilon Reshef (00:24:30):
Firstly, you as a leader need to sign up to let go a little bit, not control everything, willing to make some more mistakes than maybe you'd make otherwise. So, that's the one thing. I think the harder thing is, at least for me, is you also have to get your peers on the same boat. Because the head of sales is going to ask you, hey, what's happening? How do I know what's happening? If you don't have a control over every feature. And the CFO is going to ask you, hey, what's the, I don't know, the ROI of this, or how do you justify those type of decisions? So, there has to be some fundamental trust within you and your team, you and your colleagues, to at least experiment that way. And of course if you do it on an ongoing basis, you lose some visibility, and I think that's maybe one thing you got to acknowledge, right? If you give people more control, by definition you're going to have less visibility in what you're doing. So, give up a little bit of visibility, hopefully get the benefit of higher velocity, and higher "morale" or engagement from people, and that should result in better products as well.

Lenny Rachitsky (00:25:38):
I love that, that's a really good example. With the sales example, which is great, do you encourage the sales folks to talk directly to the pod to ask about these sorts of things, or do you discourage that sort of communication?

Eilon Reshef (00:25:51):
Oh yeah. I think sales from my perspective are part of the virtual pod. So, the core pod is as I mentioned, product engineering, but part of the virtual pod is there's product marketing, customer success, sales, in all fairness, salespeople are usually busy doing their work versus actually sitting with us and helping us, is this going to sell? Did you hear it from customers? The type of questions that product managers usually want to get, but if they're happy to spend time, they'll be very involved.

Lenny Rachitsky (00:26:20):
Coming back to the design partner way of working, does it feel crazy for companies not to operate this way, to not work this closely with design partners on new products and features they're building?

Eilon Reshef (00:26:31):
I wouldn't go back. So, I think it's just like, even I hate terms such as risks because that's a very, I don't know, ambiguous term, but just the risk of building something you're not going to know if it's going to get used. And I was asked by a very senior product manager of a very successful big SaaS companies, why do we even do this? I'm like, what do you mean? It's like, hey, we launch products and then we see if people like them. It's like I don't think that's a great idea because that company's successful, bigger than Gong, but at the same time I just think it's leaving too much in the hands of, I would even call it luck, right? Because how do you know?

Lenny Rachitsky (00:27:08):
Yeah. I was thinking it just feels like a cheat code and just feels like something a lot of companies can learn from how you all operate there. Something that has come up a bunch so far in our conversation is your focus on speed and optimizing for velocity. Something that I've heard about you is that you're really big on just making really quick decisions, even one-way door decisions that are really big, your philosophy is just make it quickly before you have all the information necessarily, talk about that approach.

Eilon Reshef (00:27:36):
That's maybe a little bit of a personal thing, but I would encourage people to look up, in Google, there's... Maybe I'll do a spoiler for Isaac Asimov, he's a science fiction writer I think beginning of last century, and he has this short story, The Machine That Won the War, so you can look it up, it's a fun story, pretty short. But it's basically the computer, the big computer at the time, supposedly won the war, but the only reason it won the war is because they wanted the people to trust this superhuman machine. But what they realized the machine was just giving crap, just like our LLM hallucinations. So, the head person, president, whatever it is, basically ended up saying, I ended up tossing a coin. But people wanted this, really believed that this is a smart machine thing is going to help us win the war. So, it's obviously a funny kind of story, but I think there is truth to it. So, many, many decisions when it's not a close call. It's like should Gong open an office in China right now? Well, probably not, there's so many reasons why not. We don't really debate it. But should we develop feature A and feature B? If you look at them, they're kind of the same, I don't know, call it same value or same cost, whatever kind of mental framework you have for deciding, you end up being like 51/49. No decision is going to be super wrong. So, yes, you can try to bring in more data and you can try to bring more people, but both decisions are okay, so just go ahead with one, hopefully it's not huge mistake. I'll tell you, I had this discussion with my co-founder Amit, who is the CO, and a few years ago we were considering buying a company, and just pretty strategic decisions. And we're like, we don't know, there's pros and cons, we're on the fence there, and we end up not buying the company. We look up Gong, and we haven't bought big companies. And I asked him, maybe it was a couple of months ago, it's like, what if we had bought that company, do you think we would've been in a radically different position? He was like, no. So, it could have been better, it could have been worse, but it would not have made a huge difference. And the reason is it was a 51/49 decision wasn't a 70/30 decision. So, it's hard for humans to make decision, you probably know, there's like experiments that show, it's almost like running or jogging or doing something that is a physical, requires your physical capacity to make decisions. So, I know it's hard that you want to postpone it, but just do it.

Lenny Rachitsky (00:29:59):
It's such a freeing way of thinking about it. It's interesting because there's been recent conversations on this podcast where Spotify has this kind of value they call talk is cheap, and it's meant to be a virtue. Talk is cheap, so let's just talk a lot before we make a decision. But it's specific to Spotify because there's a lot of regulatory challenges, and if they make it a big decision, it's a long-term, it's like they put a lot of effort into it. So, it's interesting, there's such different ways of operating. There's like, let's just talk for months and make a decision versus we're just going to make it and then it'll be fine.

Eilon Reshef (00:30:31):
Yeah, of course, like big, big, one door. Yeah, this is of course, you're going to spend more time on, but people tend to overthink I think decisions. I also found out that personally the quality of my decisions, if you sort of wake me up in the middle of the night and ask me, what do you think about X? And I'm going to be like, I have no idea, I'm sleeping. And then you're like, you got to force me to decision, [inaudible 00:30:54] make a decision, now you're going to give me two weeks to ponder over it... I don't think the quality of the decision is going to be much, much higher, which is maybe could be personal, but that's at least what I found over my too many years of existence, so.

Lenny Rachitsky (00:31:08):
I think something that's probably necessary for that to work out well is having a deep experience in that space. You've been at this for a long time, so I imagine your instinct often is trained based on your past experience of the market and customers. Do you feel like that's a necessary component of trusting your gut and instinct on these sorts of decisions?

Eilon Reshef (00:31:26):
Yeah, of course. You got at some stage know what you're doing. Yeah, if I were now to make a decision around, I don't know, entering a different space, there's no way I would be like, yeah, let's flip a coin, like the Asimov story, and go for it. I go to a conference, learn it, whatever the thing is, and then make that decision. But most of the decisions all of it make on a day-to-day basis is our domain of expertise versus totally new things.

Lenny Rachitsky (00:31:47):
Awesome. Okay, let's talk about AI for a bit. You guys were very early on AI, you were working on, basically AI was like, your product was built on machine learning back then is what it was called before. Because it was cool and everyone probably thought it was a waste of time, and no, it's never going to work. Now, everyone's building AI, building AI into their product. What have you learned about working with AI over the years that you think people maybe are not yet aware of, or that will likely cause them pain that you can help solve and avoid for them?

Eilon Reshef (00:32:18):
Yeah, funny, when we launched Gong, we didn't use the term AI because people thought it was a bad thing, it makes wrong decisions, or they just thought it's an [inaudible 00:32:26] item, an acronym. When we founded Gong, I was in sabbatical, and I actually went to this deep learning course because I was bored, in all fairness, and after that course I ended up buying Nvidia stock, which I wish I had kept up until now. But I did send an email saying, hey, this is the next thing. So, we understood it's the next thing, of course we didn't know it's going to be LLM and GPT and other acronyms that evolved over the years, and probably now that we're talking end of 2024-ish, I think people should not go from one extreme, which is, hey, we need a bunch of data scientists for every small project, which was the case five years ago, or three years ago, to the other extreme, which is, hey, LLM is going to solve everything. Because LLMs don't solve everything, they have huge utility. We use LLMs all over the place, most companies that developed AI stuff use LLMs, it's a great thing, but at the same time, don't assume it does everything, you still need some of the core competencies of AI. So, you do want to have expertise, people who actually know what they're doing, and help guide us PMs around, is this something that can be built, or no? Because if you're going to spend many, many hours on asking an LLM to do, I don't know, in the case of Gong, for example, tell me what the good sales cycle looks like? LLMs don't do that, it's just like maybe something else does, but we have a field prediction model. LLMs cannot predict fields, it's like we're very, very specialized. So, I think you still need to have expertise, you still want to have some measurements. So, yes, version one, you can just go to an LLM and say create something, I don't know, whatever, but if you don't have measurements... Like in the old machine learning, whatever metrics you use, you're not going to advance, you're going to have V1 and you're going to have V2 and you have no way to know if you've made a progress. So, we pay a lot of attention to, we have people who are going to specialize in how you measure, we use ELO system, which is the one used chess as well, and we do have experts who can help us make the right decisions. You can make a very good progress without these, but I think there's a glass ceiling if you don't figure out how to create a more operational rigor around this whole AI thing.

Lenny Rachitsky (00:34:44):
So, what I'm hearing is don't assume you can just outsource all your AI magic model building to the foundational model companies, you need to have your own AI expertise, ML expertise?

Eilon Reshef (00:34:55):
Yeah, or even if you end up outsourcing the core work, at least you have to have the expertise to understand what is doable, what is not doable, what's the right way to approach it, what's the input you get to the LLM, is this going to be good quality or bad quality? Even if you just take the product management aspect, if the LLM gives you something that is 90% accurate, or I don't know, people are going to think is good, the product's going to look different than if it's 50% good. So, just the way you even think about it, the way you... I think Figma calls their AI feature like First Draft, which is a term I like because they realize it's not best, it's not great, but it's a good first draft. So, if you know what it is, it's easier not just to name, but how conceptualize, how to build a workflow around it, and what to train users to assume for it, and I think there is an expertise there that comes on top of LLMs, even if you just use LLMs, and you can't afford or you don't want to go deeper.

Lenny Rachitsky (00:35:51):
For folks that want to do this at their company, what are the functions that you have that help you do this/skills of people you hire that you think are important?

Eilon Reshef (00:36:03):
So, I think you still have to have this kind of "data scientist role," and data scientists could be in the company, it could be advisors as well, right? Not everything has to be a full-time in the company. And the role of a data scientist is help guide the company, field prediction model, is this a LLM thing? Do you need to build a model? If you need, what input do you need? How long it's going to take, da, da, da. Also, in our world at least data scientists are the people who know how to measure these things. Is this model better or is this model better? Is this prompt better or is this prompt not better? And they're not going to do the judgment, so when Gong creates an account brief, the data scientist is not going to know if that brief or this brief is the right one, but they can guide us through what's the right tool set you need, to put it in front of customers and how do you measure this and whatnot. And then, I think at the end of the day, you also need this [inaudible 00:36:56], now it's becoming a common, the prompt engineer, the person who's actually working with the LLMs and guiding them, that is, it's a bit of a technical skill, but you got to have it. And it doesn't have to be a full-time person, but there needs to be that expertise of somebody who's actually optimizing things. Many, many customers tell us that Gong AI is, well, it's more accurate than others, yes, there is some combination of models we build from scratch, fine-tune, because we have AI expertise, but some of it is also how we, the prompt we give to the LLMs, how much rigor we put into optimizing them and kind of finding the edge cases and ranking them and improving them over time. If you want to get really good AI, you have to invest in it.

Lenny Rachitsky (00:37:39):
As you're talking, I'm thinking about how your pod model matches really well with the world of things moving so quickly, AI changing constantly, just giving teams autonomy feels like a huge advantage in this world where things are just changing weekly.

Eilon Reshef (00:37:54):
So, we have a couple of, maybe now it's three different pods, we have an embedded AI specialist team, either a specialist or a team, or I don't know, a couple of people, and then they can iterate very, very quickly on using LLMs or using non-LLMs, SLMs, people now say small language models, but whatever the thing is, they can iterate very, very quickly.

Lenny Rachitsky (00:38:15):
Awesome. Okay, a couple more things I want to touch on. One is the spiral model. So, you mentioned that you just went to learn deep learning on your own, you went off to the side, I'm going to understand this new thing that everyone's talking about, deep learning, and you got really smart in machine learning, basically, really quickly, and you have this thing you call the spiral model or the spiral method for how to learn something complex quickly. You wrote a Medium post about this, or blog post. What is the spiral method, how does it work, how do people learn things really quickly that are really complicated?

Eilon Reshef (00:38:47):
Yeah. I think it's even beyond just the speed, but also how do you even know that you actually learned it. So, there is a mathematical, or not... Physical concept called annealing, which is how certain material becomes the way it is, and it's sort of the temperature goes slightly down and eventually become crystal or whatnot. There is an element to this I think in learning as well, which is, you want to know what deep learning is, you know nothing, you go find the person next to you and you're like, what is deep learning? They tell you something, of course you don't know anything, you just heard it from one person, and the next question you should ask, who else should I be speaking with? They give you three other names... I think in tech we all tend to be, have this very, very kind cool ecosystem, people who are willing to help as long as you don't ask too much of them. So, then you speak with three other people, and then they give you other names and you sort of go around. And ideally at some stage you feel like the first person you have no idea what they're talking about, you probably didn't even understand what they're saying, the fifth person you might understand 50%, or 50% is new, at some stage you're going to feel like, well new stuff is 10%, or 5%, or 0%... I call it the spiral because it's going in circles around the target, and eventually you feel like, well, I'm hearing the same thing again and again, and you're like, well, if I heard it from three people, I didn't learn anything new, I'm at the bullseye. Of course, at the level I am, so I'm never going to be a deep learning specialist in the same way that true data scientists are, but as a product manager, I know it probably as well as I can, given that everybody I'd spoken with at the time was not giving anything new at the level that I had desired at this time.

Lenny Rachitsky (00:40:22):
I love that. Is there anything you've been studying recently that you've either used this method for or something else you're excited about learning that's new or on the cutting edge?

Eilon Reshef (00:40:32):
Usually I do this for use cases within our customer base. For example, if I wanted to, wanted to go after a certain persona, or a certain use case for the product. So, we had this notion of can we do a better job for a specific persona within sales people who are account managers? So, I would use a similar method, like, hey, talk to one account manager, talk to an analyst, or whatever the thing is, and eventually when you start hearing the same things, like what do they care about that's different than [inaudible 00:41:03] people, like selling new business or different than contact center sellers. When you start hearing the same thing, you're like, okay, I kind of got to where I need to be, now I can make decisions, I can always do another spiral and get one level deeper, which is, I don't know, do some user research, go all in, but at least at the conversation level, I've got where I need to be.

Lenny Rachitsky (00:41:24):
I love how simple this is, is you just start talking. Just find somebody to talk to, ask about this, no pressure, and then just, okay, who else should I talk to? You just keep having conversations, spiraling deeper and deeper into knowledge and wisdom. Okay, one thing I wanted to touch on, which has always stuck with me about your approach initially when you were starting Gong, is how you found your initial ICP, who to go after. And it's really funny how narrow you got when you all decided here's who we're focusing on for our first dozen customers. So, I have the list here. So, when you decided here's who we're targeting, here's the list of constraints, we're going to target people selling their product in the US, in English, over video conference, using WebEx, which was the big one at the time, selling software that is worth 1000 to $100,000, and there was only 5,000 companies in this bucket. Can you just talk about why you found it was so important to get so narrow, and just the power of getting really narrow, which is very counterintuitive to a lot of people, where they're like, oh, we're just going to be for everyone, it's a huge market?

Eilon Reshef (00:42:35):
I think it's sort of the traditional, I call it the bowling alley, or however you want to form the-

Lenny Rachitsky (00:42:42):
Crossing the chasm.

Eilon Reshef (00:42:43):
Yeah, the crossing the chasm kind of methodology, which you want to start narrow, you want to create this kind of small pond, where people talk about each other, and you can light the fire in there. In my previous company, by the way, I did read Crossing the Chasm, and I told myself, nah, I can do way better than that. So, we had one customer in, I think it was L'Oreal, or one of the cosmetics companies, and American Express, and Cisco, different industries, and there was no way we could scale it because everybody had their own lingo, the way they thought about the technology and whatnot. So, by having a smaller set of customers, or I see, definition of customers, you can develop much more focused, and then it's easier to light the fire, because people move right? At some stage, I think it was year one into the business, we heard from a company that they interviewed a salesperson, and the salesperson asked, "Are you using Gong?" And they said, "We are thinking about using Gong, but we're not." He's like, "Well, I'm only going to work for companies that use Gong." And that's sort of the power of a small pond with companies that are like each other, because you get this viral effect that is not common in B2B, but it's as close as you can because of those conversations. That other customer became a Gong customer, literally because they interviewed a person who told him he's not going to come unless they bought Gong. You can't do this if you have a wide market, where people don't even talk to each other, and there is an assumption that you're not burying yourself in this market.

Lenny Rachitsky (00:44:05):
I love... Because today, like I said at the very top of this conversation, you're just so ubiquitous, everybody seems to be using Gong. And I love that you started with something, where there was seven, I don't know, different constraints to narrow down who you're going after, and it's such a good example of the power of starting very focused and then expanding from that, which is what you've done. Okay, last question before we get to a very exciting lightning ground, we have a segment on this podcast called Fail Corner, where so many of these podcast conversations, everyone's always sharing all the successes, everything's always going great, nothing ever goes wrong, when in reality it does, things often go wrong. Can you share a story from your career or just the journey of Gong when things didn't go well, when there was maybe a failure, and if you learned something from that time, what you learned?

Eilon Reshef (00:44:54):
Yeah, I always joke that in my previous company we had done so many mistakes, that if life limited you to a certain number of mistakes, I wouldn't have any left I think. I still do mistakes, but just so many. So, every one of them probably done twice, and then it's like at some stages, third time's a charm. So, the one I just gave you is probably the worst, is crossing the chasm, you start a company, you have this technology, I was thinking let's go horizontal. And that technology was whatever, web integration, something, eventually ended up being an e-commerce content syndication, or [inaudible 00:45:28] management SaaS software, which is the right way to go because you want to specialize in a certain market. But initially, just going on in was just ridiculously not smart, and the other thing we did together was that was, the previous company started year 2000, so that was the bubble, one of those very, very nice bubbles. So, we're like, you know what? We actually got three customers, admittedly in totally three different segments, now let's go and scale. Now, we all knew we need one salesperson, one SE and [inaudible 00:45:59] what's now called product market fit, I don't know that the term even existed there, and we're like, nah, you know what, investors told us you got to hire more people. So, we hired, I don't know, 20 salespeople, all of them failing miserably, because A, we didn't have a true product market fit, but even what's worse, we didn't have a true focused ICP with a very, very repeatable product market fit. So, if you sort of hear me talk about how we started Gong, Amit is the CEO, and he drove a lot of that business strategy, but me being sort of a co-pilot there, it definitely bringing the same, I'm not going to make that mistake again, I might do new and fun ones, but not that same mistake again.

Lenny Rachitsky (00:46:36):
Awesome. Thank you for sharing that. With that, we reached our very exciting lightning round, are you ready?

Eilon Reshef (00:46:42):
Sure.

Lenny Rachitsky (00:46:43):
Let's do it. First question, what are two or three books that you find yourself recommending most to other people?

Eilon Reshef (00:46:50):
There is a set of books, I think one that is the starter one is, I think it's called, right now, the Ideal Executive. People don't really know it, it's sort of a management book, how to run a team and whatnot. I think the original version is, funnily enough, I think it was called Mismanagement, but nobody wants to buy a book called Mismanagement, you'd much rather buy a book that's called Ideal Executive. Because you, of course, are not mismanaging, you're the ideal executive altogether, so you're just reinforcing your self. But jokes aside, it basically gives you the... It tried to define people by four characteristics, I think misnamed, but are you an administrator? Are you, he calls it a producer, basically get the job done? Integrator, which brings people together, and the fourth one, it's basically change agent, do a lot of mess and change stuff. Usually entrepreneurs kind of include that part, of course. And basically, his claim is that nobody does the whole four, maybe you're good at one, maybe okay at the other, and personally I'm horrible in administration. I obviously acknowledge that, and I try to sort of compliment myself. So, I think there's two things in it, firstly, just those, I thought there was the four good ways of looking at people, as a manager, as a leader, of course, that's one, but I think even if you disagree with those four, just understanding that you want to look at the people in the organization, yourself included [inaudible 00:48:20] key characteristics, and you can select the different framework, helps you a lot with creating high-velocity discussions with others. Because I can talk with somebody and say, hey, you're a P. He's going be like, well, I'm not P, an I, whatever the thing is, and that makes a discussion that is much, much faster, and more comprehensive than just trying to explain this from scratch. Like, hey, you tend to do this, and you might want to do this, and you might want to strengthen that. So, I'd recommend starting from this, but there's probably other methodologies you can pick, and maybe some of the listeners here have already had one, but that's one I like because I found it useful.

Lenny Rachitsky (00:48:57):
And it's called the Ideal Executive?

Eilon Reshef (00:48:59):
I think so, I'm pretty sure. Yeah.

Lenny Rachitsky (00:49:01):
Great. Any of other books before we move on?

Eilon Reshef (00:49:05):
That one's probably-

Lenny Rachitsky (00:49:06):
That's the one.

Eilon Reshef (00:49:06):
I like Crucial Conversation, that's going to, in the beating path, it's like how to conduct conversations with people in your organization. I think it's never bad to-

Lenny Rachitsky (00:49:16):
[inaudible 00:49:16].

Eilon Reshef (00:49:16):
... reimmerse yourself into how to speak properly with other people.

Lenny Rachitsky (00:49:20):
We have an episode coming up where we're going to share scripts and phrases to use to have better hard conversations.

Eilon Reshef (00:49:27):
Ah, it's good.

Lenny Rachitsky (00:49:28):
Yeah, I'm excited for that/scared. Okay, next question, do you have a recent movie or TV show you've really enjoyed?

Eilon Reshef (00:49:35):
I didn't have TV, like broadcast TV for many, many years, so nowadays there's Netflix so you can find stuff. But my taste in TV and movie tend to be pretty esoteric, French. So, I've recently watched this British TV series called Slow Horses, with Gary Oldman, and it's a really kind of fun sort of funny spy thing, which I found amusing and intelligent at the same time. So, some kind of comedies tend to be pretty lowest common denominator, that one seems still fun and witty at the same time. So, that's my latest that I really enjoyed watching even this third seasons.

Lenny Rachitsky (00:50:14):
I love Slow Horses, it's like... I don't think it's that obscure, I think it's one of the ones Apple promotes often. I will say this, last season was not my favorite, but the other two were awesome.

Eilon Reshef (00:50:26):
Yeah, I 100% agree, which I said, even the third season was okay, but the first two were really, really good and-

Lenny Rachitsky (00:50:31):
Yeah. It's super fun.

Eilon Reshef (00:50:32):
... [inaudible 00:50:32] the fourth.

Lenny Rachitsky (00:50:33):
It took me like three tries to actually get into the show initially, because people kept telling me it's so good, and I started watching, and it's just like, who's this old messed up guy, just complaining endlessly? But you got to keep watching. Okay. Do you have a favorite product you've recently discovered that you really like?

Eilon Reshef (00:50:47):
I assume you have a silverware caddy in your dishwasher, right?

Lenny Rachitsky (00:50:53):
Oh yeah, to put forks and knives. Yeah.

Eilon Reshef (00:50:55):
The cutlery... So that's my favorite product as of lately, and I'll tell you why. It's a funny story, I lost mine, and you can ask yourself, how can you freaking lose one of those baskets? And it was in the dishwasher, of course, and for some reason I couldn't find it, that's like you have to be really out of your mind to not find. Anyway. So, I go to some Amazon or eBay, wherever, I just buy a new one, and then of course a day later I find it's [inaudible 00:51:20] somewhere within the dishwasher. Now I have two. So, this is my latest invention, if you have two of those baskets, you can put one of them in the sink and you can just continuously load your cutlery or silverware while the thing is working, or you haven't vacated it. So, it kind of changed how we organize our kitchen with something that probably costs $10. No product manager has ever thought about offering two of those with your dishwasher, I don't think it even tried to upsell any of that. And I told it to some people and they actually ended up buying a second one, and said it was successful, which is the most ridiculous thing, it's like spend $10, $15, get something organized in a completely obscure and unintentional way.

Lenny Rachitsky (00:51:59):
I'll give you an even crazier idea that a previous guest suggests, Rory Sutherland has this pitch that you should have two dishwashers, everyone should have two dishwashers, because one is your clean and one is dirty. And you just take your plates and things out of the clean one, use it and put it straight into the dirty dishwasher. And why are we just putting things away constantly, just like go from one to the other and one to the other? So, there you go.

Eilon Reshef (00:52:27):
Similar idea.

Lenny Rachitsky (00:52:28):
Similar idea, next level.

Eilon Reshef (00:52:29):
Mine is like $15 though, a little bit, maybe cheaper.

Lenny Rachitsky (00:52:31):
Yeah, exactly. Houses are not designed for two dishwashers. Okay, two more questions, do you have a favorite life motto that you often come back to, find useful in work or in life?

Eilon Reshef (00:52:42):
One that I use, it's going to sound funny, but it's actually real and I use it, and I actually believe in it. It's, I'm not sure if you know for philosophy, there's like razors, like Occam's razor, which is basically-

Lenny Rachitsky (00:52:53):
Oh, there's other razors.

Eilon Reshef (00:52:54):
Yeah, there's so many razors, and there's one that I think came in in some Murphy book or whatnot, and it's called Hanlon's razor, you can look it up, Wikipedia or wherever. And it basically says, it goes like, "Never attribute to malice, that which is adequately explained by stupidity." So, it obviously sounds funny, and it's trying to be funny, but it's so helpful because so often do we attribute people's behavior, think in a company, customer, I don't know, personal life sometimes, to malice like, oh, this person's not returning my calls because X, or this person hasn't given me feedback or has given me feedback because of X. And it's sort of like we all, I think there's a saying, it's like always assume well, or good intent, or whatever, and this is sort of the more funny way to sort of say that, yes, the person is... And again, stupidity is obviously a funny way to do it, maybe inappropriate. But it's basically, yes, they just didn't know, they didn't care, they didn't think about it, they weren't trained, whatever the thing is, and if you take this model on your day-to-day life, at least I find that it's so true, and so often true, that is funny, but inspiring.

Lenny Rachitsky (00:54:02):
I really love that quote. I think of it often when somebody's doing something that's annoying me. Final question, you mentioned that you are from Israel, you live in Israel, you mentioned delicious food, hummus is one example. Is there another Israeli food that you think people are sleeping on, that you think people should try when they have a chance?

Eilon Reshef (00:54:21):
Israeli food has become a little bit to be in fashion lately, so people coming from the US to visit us in the office are like, oh, Israeli food is so good, and I'm like, what do you mean? It's the same food we've had for 20 or 30 years. I think the taste change because you kind of eat more healthy and less oil these days. Most of Israeli food is sort of Arabic in nature, or Turkish, so there's great falafel, great hummus, pita bread, Turkish delights of sort, so a lot of those. And some very, very obscure, and if you come to Israel, I'll show you around some very less known food that only special guests get to taste. I can't say here because-

Lenny Rachitsky (00:54:59):
What's one... Yeah, say it here, [inaudible 00:55:00].

Eilon Reshef (00:55:01):
There is a thing called Sabich, for example, nobody knows of it. People claim it came from the people who came from Iraq, but my wife's father came from Iraq, he's like, we've never seen this before. It's sort of pita bread filled with hummus and eggplant and eggs.

Lenny Rachitsky (00:55:16):
Oh wow.

Eilon Reshef (00:55:17):
And maybe something else, I have no idea. Tahini, maybe. I don't know. It tastes good, but it's such a weird combination, and it's become a little bit of a thing, and nobody knows what the origin is. I think somebody made a mistake and gave you the name, and now it's like ubiquitous.

Lenny Rachitsky (00:55:32):
You are making me hungry. Eilon, this was amazing. Two final questions, where can folks find you if they want to reach out and learn more, maybe ask some follow-up questions, and how can listeners be useful to you?

Eilon Reshef (00:55:43):
I'm pretty available, and LinkedIn is probably the best way. I tend to read my inbox in LinkedIn and respond when I can. And then useful to me, if you want to come work for Gong, check out our careers page, of course. The product team is mostly based in Tel Aviv and Dublin, Ireland, so maybe a little bit remote for most people, but there's sometimes folks in the US and sometimes non-product, of course, roles. We're hiring quite a few people these days, so we'd love to at least give us a chance.

Lenny Rachitsky (00:56:11):
Awesome. Eilon, thank you so much for being here.

Eilon Reshef (00:56:14):
Thanks for inviting me.

Lenny Rachitsky (00:56:16):
Bye everyone. Thank you so much for listening, if you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at Lenny'sPodcast.com. See you in the next episode.
