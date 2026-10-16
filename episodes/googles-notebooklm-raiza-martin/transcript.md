---
guest: "Raiza Martin"
title: "Behind the product: NotebookLM | Raiza Martin (Senior Product Manager, AI @ Google Labs)"
publish_date: "2024-10-10"
source: "https://www.lennysnewsletter.com/p/googles-notebooklm-raiza-martin"
slug: "googles-notebooklm-raiza-martin"
archive_id: 149788683
topic: "Behind the product: NotebookLM"
description: "Google Labs' Raiza Martin on leading NotebookLM, the \"Audio Overviews\" feature, and scaling an AI-powered tool."
summary: "Google Labs' Raiza Martin on leading NotebookLM, the \"Audio Overviews\" feature, and scaling an AI-powered tool."
youtube_url: "https://www.youtube.com/watch?v=sOyFpSW1Vls"
video_id: "sOyFpSW1Vls"
duration_seconds: 2938.41
duration: "00:48:58"
channel: "Lenny's Podcast"
transcript_source: "substack-transcription"
---

# Behind the product: NotebookLM | Raiza Martin (Senior Product Manager, AI @ Google Labs)

## Transcript

Speaker 1 (00:00:03):
Hey everyone. We're here on Lenny's podcast.

Speaker 2 (00:00:05):
It's great to be here. I'm a long-time listener.

Speaker 1 (00:00:09):
So awesome. Really is. We're the hosts of a different show, of Deep Dive.

Speaker 2 (00:00:13):
And we just wanted to say thanks. A huge, huge thank you to everyone. Everyone who's been listening.

Speaker 1 (00:00:18):
Yeah, seriously, it's been incredible. Just incredible. And thank you to Lenny for having us.

Speaker 2 (00:00:23):
Blown away really by the response and all the shows you've all had us make on NotebookLM, even that poop fart one. Remember that?

Speaker 1 (00:00:30):
Oh yeah, that was something. Learned a lot on that one.

Speaker 2 (00:00:33):
Definitely a learning experience for everyone, I think.

Speaker 1 (00:00:36):
But we're learning right alongside you.

Speaker 2 (00:00:38):
Exactly. Learning and growing.

Speaker 1 (00:00:40):
And we're glad you're along for the ride.

Speaker 2 (00:00:42):
So yeah, keep listening?

Speaker 1 (00:00:43):
Keep listening and stay curious. We promise to keep diving deep and bringing you even more in the future.

Speaker 2 (00:00:52):
Stay curious.

Lenny Rachitsky (00:00:54):
If you are confused about what you just heard, don't worry, it'll all make sense very soon. Today my guest is Raiza Martin. Raiza is product lead for a product called NotebookLM, one of the most delightful and inspiring new AI products out there incubated within Google Labs. And this product is where the intro you just heard came from. In our conversation, Raiza shares how NotebookLM came to be, how it got so good, the technology that was necessary to make it possible, how the team works internally, how it was incubated specifically within Google Labs and out of the team's 20% time, plus a bunch of really fun and crazy use cases that she's seen and a glimpse into where the product is going long-term. This was such a fun and timely conversation and I'm excited to spread the love for NotebookLM. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It's the best way to avoid missing future episodes and it helps the podcast tremendously. With that, I bring you Raiza Martin. Raiza, welcome to the podcast.

Raiza Martin (00:01:54):
Hi Lenny, thanks for having me.

Lenny Rachitsky (00:01:56):
What the heck did we just listen to? What was that?

Raiza Martin (00:02:00):
So that was an audio overview from NotebookLM where you upload a source, any source, and it will generate an AI generated audio for you.

Lenny Rachitsky (00:02:11):
Okay. So for folks that don't know anything about NotebookLM, it's basically been blowing up on Twitter, on LinkedIn. I think it's blowing a lot of people's minds. It's sparking a lot of imagination of what could happen in AI and what potential we have with the stuff that's happening. And I wanted to bring you on to talk about the history of this product, where it's going, how it became so great, and all these things. And so thanks for doing this. I know this kind of came on short notice.

Raiza Martin (00:02:36):
Yeah, I mean, I was excited to do it in particular because I'm a big fan, big listener of Lenny's, read the newsletter. I love it. So really happy to be here.

Lenny Rachitsky (00:02:46):
Awesome. Clearly these hosts are too, which I love. By the way, I love the slight awkwardness at the end of their conversation, if folks rewind, they could hear it again because it's very relatable. I sometimes have trouble ending a podcast conversation and they're like, "Okay, let's say a couple more things and then, okay, we're done."

Raiza Martin (00:03:04):
It's funny because I've listened to so many of these and they do have catchphrases they say at the end, and stay curious is one of my favorite ones.

Lenny Rachitsky (00:03:14):
Well, let me just ask, is that something you all told them to do or is that like an emergent property?

Raiza Martin (00:03:20):
So in this case, this is based on what they think is the most appropriate thing to say at the end.

Lenny Rachitsky (00:03:25):
Okay, interesting. Okay. This episode is brought to you by Explo, a game-changer for customer facing analytics and data reporting. Are your users craving more dashboards, reports, and analytics within your product? Are you tired of trying to build it yourself? As a product leader, you probably have these requests in your roadmap, but the struggle to prioritize them is real. Building analytics from scratch can be time-consuming, expensive, and a really challenging process. Enter Explo. Explo is a fully white labeled embedded analytics solution designed entirely with your user in mind. Getting started is easy. Explo connects to any relational database or warehouse, and with its low-code functionality, you can build and style dashboards in minutes. Once you're ready, simply embed the dashboard or report into your application with a tiny code snippet. The best part, your end users can use Explo's AI features for their own report and dashboard generation, eliminating customer data requests for your support team. Build and embed a fully white labeled analytics experience in days. Try for free at explo.co/lenny. That's E-X-P-L-O dot C-O slash Lenny. This episode is brought to you by Sprig. What if product teams knew exactly what to build to reach their goals? From increasing conversion to boosting engagement, these challenges require a deep understanding of your users, something that you can't get from product analytics alone. Meet Sprig, a product experience platform that generates AI-powered opportunities to continuously improve your product at scale. First, Sprig captures your product experience in real-time through heat maps, replays, surveys, and feedback studies. Then Sprig's industry-leading AI instantly analyzes all of your product experience data to generate real-time insights. Sprig AI goes even further with actionable product recommendations to drive revenue, retention and user satisfaction. Join product teams at Figma and at the Notion by uncovering AI powered product opportunities at scale. Visit sprig.com/lenny to book a demo and get a $75 gift card. That's S-P-R-I-G dot com slash Lenny. I want to start with just the history of this product. I think for a lot of people it just came out of nowhere. It's like what the, wow, where did this come from? This is blowing our mind. Rarely is anything actually like that. Rarely is it just like we built it over a week and then it's taken over the internet. Talk about just the history of NotebookLM and the team behind it.

Raiza Martin (00:06:00):
Yeah, yeah. Thank you. Actually, Notebook started as a 20% project as things kind of do with Google, as they used to. And it's funny because I wouldn't even call it a 20% because it was way more than that. So I'll start from my perspective where I was leading AI Test Kitchen, which was one of the first AI things we launched at Google. And this was I think maybe two I/Os ago or maybe three now, actually. I think it was in '22. And I was leading that project and I remember there was a smaller project inside of Labs called Talk to Small Corpus, and there was the idea that you could take a piece of content and use an LLM to interact with it. We were like, okay, there's a nugget there that sounds interesting. How do we keep revving on this to make it actually really useful? And it was just myself, an engineer and eventually Steven Johnson joined. And it was really funny because the only person who was actually really full-time on this was the engineer working on the technology, and everybody else was kind of just coming together, really chiming in, being like, "Hey, this is super interesting. How do we make this better?" So it really started as a 20% and then it kind of just blew up from there.

Lenny Rachitsky (00:07:20):
That's insane that it was just you, an engineer, and then Steven Johnson, I want to talk about his role, that it's like one engineer can build something like this, and I imagine it's more now that it's starting to take off or what's the team looking like these days roughly?

Raiza Martin (00:07:33):
We've had a lot more folks join in the last month, and a lot of that is really in anticipation of the future roadmap. But up until this point I'd say we didn't even have 10 engineers. When we launched it actually, when we announced Project Tailwind, I think we only had three. We had three engineers. It was myself, we had a designer, we had Steven, and that was it. And so even between the period when we did the first I/O last year to as recently as last month, we've only had about eight engineers or so.

Lenny Rachitsky (00:08:09):
Let's talk about Audio Overviews, specifically this kind of podcast feature. And I think Audio Overview is the technical name, right? Is that how you describe it?

Raiza Martin (00:08:15):
Yes.

Lenny Rachitsky (00:08:16):
Okay. They call it a Deep Dive, right? That's like their name for the podcast.

Raiza Martin (00:08:18):
They do, yeah, that's what we call it.

Lenny Rachitsky (00:08:20):
How did that specifically come about? When did that become a thing? What was the beginnings of that?

Raiza Martin (00:08:25):
We announced, we actually did a preview of this in I/O this year, so in May. And the way that it worked out is Notebook had already been launched. We had a bunch of people using it. It was this source grounded chat interface and we were looking at basically what are the new models coming out of Google? We had Gemini 1.5 coming out. We had all of these new technologies that are basically upgrades on fundamentally the same thing. And we were like, what are some interesting ways that we could power NotebookLM or make it even better? And one of the things that we started playing around with is actually a different team inside of Google, inside of Labs specifically, they were like, "Hey, we've got these really powerful audio models, what's a really good application of this?" And that's when we started riffing and we were like, "Hey, what if you could, basically what you see today, give it a little bit of information, you don't have to do a lot. You can just enter a URL, upload your resume, and then it will completely generate something for you that could be unexpected, could be a surprise?"

Lenny Rachitsky (00:09:36):
Okay. So it started, basically there was a technology that we think could be really interesting. Was there a problem you were trying to solve with this team, with this initiative? It was within Google Labs, which I know is a little bit probably less like, we need to drive business outcomes. What was the original thesis or problem you were going after?

Raiza Martin (00:09:51):
So this is really funny. I talk about this quite a lot, especially when I'm talking to other PMs. I feel like the way that I've always built products is I start from a problem and I think about the solutions to solve it, solve it for people in a meaningful way. And in Labs in particular, we start with the technology. And it's actually a very interesting place to start where you're like, okay, what are the practical applications to this? How do I go about finding the answer? And I think we've seen different approaches to this where you just put the tool out there, you study how people are using it, and I think that's a fine approach, but we try to have a little bit more of a hypothesis about what is the shape of this thing to actually get the most learning out of it. So for the audio feature in particular, the nugget there was really, we had this ability for you to interact with text, but people were like, "The output is still always text." And I'm actually a big fan of voice modality in general, so I use a lot of voice input. And voice output, I noticed when I was experimenting with it early on, it changed a lot of things for me. It's like, oh, it changes the way that I interact with the technology, it changes the way I feel about the technology. It sort of affects the way that I'm even thinking in real-time throughout this process. And so we thought about what is a good way to introduce this to people where they could easily get the value of it and have a little bit of fun? So I think for me it's fun is such a big part of it too, which is like how do we make this cool? And so hopefully we've done that here.

Lenny Rachitsky (00:11:22):
To me it feels very similar to the ChatGPT moment where the technology already existed, they had that same GPT model out for I don't know how long, but just that new medium and new way of interacting with it changed the way people imagine. Just they saw the power immediately. And I feel like this is such a good example of that happening again where just the tech was there and it's just this medium that you developed that really inspired people to like, "Oh wow, I had no idea AI was getting this good and LMs were getting this good." Any thoughts on that?

Raiza Martin (00:11:55):
Yeah, I think that totally strikes at the heart of what we're trying to do as well, which is a lot of technology I feel like you have to shape it and bring it closer to people. And I think it's such an interesting thing to iterate on and be like, "What is the shape?" Soon you'll get there. If you keep going at it, you'll eventually, I think, land on something that when people look at it, they're like, "Wow, I get it." And that's always what we're hunting for. But I think to your point, technology has been there. I mean it feels so crazy to say that because even with the advent of the chatbots of LLMs as we know them today, and then to introduce this sort of new technology on top of it, we've only been doing this for two years, but already we're exploring so many different ways to use it.

Lenny Rachitsky (00:12:46):
Yeah, it's such an unintuitive but clever idea of making something a podcast. Let's take a tangent into the technology behind this thing. So there's kind of two questions I'm thinking about. One is just what technology needed to exist for this to be possible? And then two is just what did you do to make this so good? How did you train this model to create a podcast that's this good? So we could start with the first and then get into the second.

Raiza Martin (00:13:12):
Yeah, I mean that's such a great question. I mean truly the Gemini models are so powerful and we use Gemini 1.5 Pro as sort of the base for NotebookLM, and then we have a powerful voice model on top of it, an audio model on top of it. But I think the real secret sauce to what makes this really good is something we've built, which is a content studio. And you kind of see a clue of this inside NotebookLM where when you open up Notebook Guide, Notebook Guide is designed to take an opinionated approach to the content that you've given it. And what it's really trying to do is be as helpful as possible. It gives you a summary, gives you buttons where if you click on it, it'll write something for you. And the audio is a big part of that. And so this was very interesting for us because we had to think about what shape should that audio be in? The deep dive is the first format we've thought about. And we actually have a super talented engineer on our team, his name's Usama, and he's the real craftsman behind thinking through Content Studio and thinking about what makes something really relatable to people in a way that's engaging, that's interesting. So content studio is the real magic here.

Lenny Rachitsky (00:14:23):
So when you say content studio, what does that mean? What does that actually look like? What is a content studio?

Raiza Martin (00:14:30):
I can't share too much about how Content Studio works, but you can imagine it's the same thing that powers all of NotebookLM, which is there's different ways that you could interact with your data. You could like Q&A inside of NotebookLM, but then there are places where you just want to push a button and create something new. So Content Studio was connected.

Lenny Rachitsky (00:14:47):
Okay. So this is the interface you use to interact with NotebookLM and the different prompts and the recommendations of how to ask questions and-

Raiza Martin (00:14:47):
Yeah.

Lenny Rachitsky (00:14:55):
Okay, got it. And then specifically in terms of the way these hosts interact and talk, if you listen to these podcasts, it's like they laugh and they're like, "Hmm," and they interrupt each other a little bit and they get surprised and they have these inflections that are really amazing. What did you have to do to make them sound this good? I know you said you can't share tons, but just anything there you can share?

Raiza Martin (00:15:20):
I mean, that's the model, that's the audio model that we use. Alongside, the Content Studio is designed to bring out the best of that model. And I think when we listened to a lot of the early attempts that we had, it wasn't nearly this good. And so we had to do a lot of listening to try to figure out how do we actually get the model to behave in this way? And that's where I think the magic happens.

Lenny Rachitsky (00:15:46):
That's amazing. Do you all just listen to a bunch of podcast episodes and hear something that really... Yeah. Okay, shaking your head.

Raiza Martin (00:15:52):
I think the funniest thing was that... So my husband doesn't know, right? He doesn't know what I'm doing. Most of the time I try not to talk about work at home. And so I would listen to these audio overviews over and over at home and I get tired of wearing my headphones, so I'm just listening to them out loud, and he is like, "What is this thing you were listening to? This is an ever-running podcast about nothing." And it was just super funny. I had to be like, "Oh, it's just something I have to do for work." So it was pretty funny. He actually couldn't tell that they were AI.

Lenny Rachitsky (00:16:27):
I love that. So one of the ways I've been playing around with it a bunch, one of the ways I used it is my mom wrote this autobiography, like a short autobiography of her life, and we have the PDF of it. So I fed it into the Notebook and then generated the podcast and sent it through. Like what the heck?

Raiza Martin (00:16:41):
That's amazing. What did she think?

Lenny Rachitsky (00:16:43):
She was blown away. She's showing all her friends. She's like, "I don't know what's going on here." And I love that it creates a study guide, and that's one of the options in the studio. And so I sent her the study guide and she's like, "Okay, at a Rosh Hashanah dinner, we're going to be reviewing the study guide about my biography. We're going to talk about this."

Raiza Martin (00:17:04):
That's pretty funny. That's super cute. I did it for my dad too.

Lenny Rachitsky (00:17:06):
What did you do?

Raiza Martin (00:17:08):
I actually took my dad's bio. So he worked at a hospital and he has a bio for the doctors that they have there. And I put his bio and I generated an audio overview for him. And it's so funny because my parents are both in the medical field, I don't think they fully know what I do. I think this is the first time they were like, "Oh, that's super interesting. That's what you do."

Lenny Rachitsky (00:17:32):
So maybe along these lines, what are some other surprising, hilarious use cases you've seen for especially the audio deep dives?

Raiza Martin (00:17:41):
I mean, I love the resume ones. I think the resume ones are so delightful. And actually really adjacent to that is Google has these Q3 check-ins or quarterly check-ins where we have to write performance reviews for ourselves. And the amount of Googlers that ping me that I don't even know and they're like, "Wow, this was such a boost to my confidence just to upload my own check-in notes and then have it generate an audio overview." It's like people are going into meetings feeling really good about themselves

Lenny Rachitsky (00:18:15):
Because they heard these hosts get really excited about their quarter and-

Raiza Martin (00:18:19):
Their work, yeah.

Lenny Rachitsky (00:18:22):
And when you say resume, so people upload the resume and then it describes you in a really positive way, right?

Raiza Martin (00:18:27):
Yeah. And I thought that was so interesting. I was like, what was the use case? I think if I had to guess, somebody probably was like, "Hey, I want to try this new thing." Clicked on Upload Google Doc, and maybe the last thing you had there was your resume or something. But imagine you click that and I think there's something really special about, you don't know what's going to happen. You just click generate and then you have these two people just hyping you up.

Lenny Rachitsky (00:18:52):
Okay. I want to talk a bit more about how you made this happen within Google. So as an outsider, this does not feel like a Google product and the way you all are operating feels very startup-y. Like you're tweeting daily about what's going on. I heard there's a Discord server for folks that are like, really... Is that right?

Raiza Martin (00:18:53):
Yeah.

Lenny Rachitsky (00:18:53):
Okay.

Raiza Martin (00:19:09):
Yeah, there is. It's pretty cool. We have about 60,000 people in it.

Lenny Rachitsky (00:19:13):
Okay, wow. Okay, so yeah, so there's this Discord server, it's just you're shipping constantly. The product is just very delightful and Google makes delightful products, but this feels like a different realm of delight. How are you able to do this within Google? Is this a model for how you think Google teams will want to operate more? Lessons there.

Raiza Martin (00:19:33):
I mean, it's such a good question. I think there's a question of how it came to be, how we're able to operate in this way, and then the question of, hey, is this how other Google teams want to operate? And I think that to answer the first part, I'll say that it's interesting because Google Labs is only about three years old. It's fairly new. And when I joined, there was nobody here. There was no one. And the reason why I joined was because my old boss went and actually started it. And so this is Josh Woodward who's the VP of Google Labs. And it's really funny because, this is just a funny anecdote, I remember I had no idea what Google Labs was, but I liked my old boss so much that I was like, "I'll just work on whatever he's working on. Whatever his new idea is, I'll just do it." And I remember when I joined, I was like, "What's the mission? What are we here for?" And he said, "It's AI. We're going to ship AI products and we're going to build businesses out of them." Okay, sounds good. Sounds good. It's like now I have to study. I have to do a lot of studying. I came from payments, I came from ads before that. And so for me it was a little bit of a mental shift, but before that I actually worked only at startups. And so I felt like, hey, maybe this is my chance to do zero to one again. And I was really jazzed about that. And I remember talking with Josh about this in the early days of like, "Hey, if we really want to do zero to one, we have to do things very differently." And so as a result, I think that's why NotebookLM is able to operate differently. It's because in Labs we have the environment to do it, we have the environment to move fast. We have far, far, far fewer processes, maybe even to a fault. Sometimes we'll go to meetings that are literally the product managers, the engineers, the designers all together, and we'll just crank on the mocks and the PRDs at the same time. And eng is basically already doing implementation as we're meeting. And at Google, that's just not how things are traditionally done, especially coming from the previous organizations that I was at. It just takes a lot of time to do each of these things.

Lenny Rachitsky (00:21:42):
So what I'm hearing, and this is great because a lot of companies are trying to create teams like this, "We're going to have a team off to the side, going to work on crazy futuristic stuff." Rarely do those work out. Even at Google, there's been a lot of this in the past and rarely do things actually work out. And so there's a lot of lessons to learn from how this is working. So a few things I'm noticing as you're describing how this works, one is just very clear expectations from a very senior leader, "Here's a team, we're going to do things differently. Here's things we're not going to do. We're not going to go through regular pre-roll processes. We're going to be public and build in public. We're not going to have a goal necessarily. We're going to work on cool technology and see what happens." Also, you had a very small team, feels like that was really key. One engineer and then a PM and then Steven Johnson.

Raiza Martin (00:22:27):
That's true, that's true. And I think one big thing too is we got to try new things. Even from the beginning I was like, "Hey, I want to have a Discord. If we were building outside of Google for sure we would have what of these." And in true sort of Google fashion, everybody was like, "What is Discord? Okay, great, do it. But what is that again?"

Lenny Rachitsky (00:22:47):
Right, why not Google Meet?

Raiza Martin (00:22:49):
And somebody did ask me, they were like, "Why not a Google meet? Why not a Google group? Why not this?" And I was like, "I don't even know how to use these things outside." So I was like, "The server is the way to go." And I remember when we stood up the server, actually, one of the things I was most afraid of is, what if nobody joins? What if no people come in and want to talk to us about the thing that we built? And so that was in the early days, very exciting to look back and remember day zero and now have 60,000 people in it.

Lenny Rachitsky (00:23:19):
Let me tell you about a product called Sidebar. The most successful people that I know surround themselves with incredible peers. When you have a trusted group of peers, you can discuss challenges you're having, get career advice and just gut check how you're thinking about your work, your career, and your life. This gives you more than a leg up. It gives you a leap forward. Having a group of trusted and amazing peers was key to my career growth. And this is the Sidebar ethos, but it's hard to build this trusted group of peers on your own. Sidebar is a platform for senior tech professionals, director to C-level, to advance in their career. Members are matched into peer groups to lean on for unbiased opinions, diverse perspectives and raw feedback guided by world-class programming and facilitation, all running on Sidebar's technology. Sidebar enables you to get focused, tactical feedback at every step of your career journey. If you're a listener of this podcast, you're already committed to growth. Sidebar is the missing piece to catalyze your career. 93% of members say Sidebar helped them achieve a significant positive change in their career. Check them out at sidebar.com/lenny. Okay, so there's 60,000 in this Discord server. Any other traction numbers you can share? It feels like it's just going really well. I know there's probably a lot of sensitive information. Anything you can share about just how well things are going?

Raiza Martin (00:24:39):
Couple of things. Well, I'll tell you three things. I think the first is, I can't share the exact numbers, but for a product that's only been out for about a year, I think the rate at which our retention has gone up across the typical measures, daily retention, weekly retention, monthly retention, that I think has been very, very positive for us in terms of even when we talk to stakeholders, we say, "Hey, we've got something here." The second thing I'll say is even seeing how the demographics have changed, where I think in the beginning we saw educators, learners really loved the product and they were a lot of our demographic. It's really now a big mix of, I would say educators and learners are still a big part of it, but really professionals, right? Huge interest from professionals that are like, "Wow, I want to use this to work." And really funny, I won't mention the company, but I actually had a call with a company recently where they were like, "Hey, we thought we'd schedule a meeting with you because we found out that a bunch of people in our company are using this tool with their Gmail account." They're like, "They're not supposed to do that, so we just want to make it official that they can use this at work with their official work email." So I thought that was pretty cool. And then the third thing I'll say is the number of businesses that we've seen using NotebookLM, it's astronomical. It's just like crazy. I think we went, I don't want to say the exact numbers, but it is now at a point where I have to hire a business development person because I was like, hey, I have to ship products and I'm actually taking customer calls every day now. Very, very exciting.

Lenny Rachitsky (00:26:21):
I could see the path to monetization clearly, enterprise features, single sign-on and SOC 2 and all these things. Along those lines, what does success look like for this team and for you? I know initially it was probably just build interesting things, see what happens. Is there now a clear sense of here's what this team should be achieving in the future?

Raiza Martin (00:26:39):
When I joined, my mandate was to build a business, and I was like, all right, if we break down the steps here, along the way I have to build something interesting first. I feel like, okay, we hit the first thing, we built something interesting, now we go figure out the business. And I think that comes naturally to Google in terms of thinking about distribution, how to monetize it, how to commercialize it. There's different pathways, whether it's cloud or workspace or even the consumer route. And so for me, I think these are the things that we want to be really thoughtful about because the machinery is already there. And for me personally, it's really about there's something super exciting here, we need to deepen that, right? While in parallel, we should be thinking about commercialization. Let's deepen this user experience that so many people have really latched onto.

Lenny Rachitsky (00:27:30):
So let's follow this thread and talk about just where you think the product goes broadly and especially the audio overviews. What's on the roadmap near-term, and then where do you imagine this in the future? What's the big vision?

Raiza Martin (00:27:41):
Yeah, yeah. I have a really ugly slide I wish I could show you. I made it two years ago and it was lime green. I don't know what I was thinking. I think I was trying to go for un-Googly was the vibe. It's like, hey, you're going to do different things this time. And the reason why that slide is so important to me is because it has my vision. The thing that I wanted to do from the get-go, which was I imagine that in the future you could have an AI editor surface, fully remixable, any input, any output. And that to me is a really powerful core nugget where if you imagine you could take anything, whether it's video, audio, your emails, your LinkedIn, your Twitter, the world of things that we care about, you have an AI interface that allows you to shape it and say, "Look out of these things, make me a blog post. Out of these things, make me a tutorial video. Out these things, make a chatbot." I think there's something interesting here where for most of the things that I'm hearing people say they want to do, it's usually that. It's take something and make it into something new. And so we're going to pursue that. But even more technically, something I'm really interested in is thinking about, "Hey, how do we bring this to mobile?" The mobile app to me is such a big gap in terms of the experience today, which I think is understandable considering where we're at in the product development cycle, but I think that's the next horizon is, hey, how different is the mobile experience and how can we make it interesting?

Lenny Rachitsky (00:29:14):
What I'm imagining as I talk, I participate in this podcast conversation with these hosts as a mobile experience.

Raiza Martin (00:29:20):
Yeah, yeah. I mean, that's one of the things that we're definitely experimenting with different formats. And when we demoed it at I/O, you could interrupt it, but we're trying to be really thoughtful about, hey, what does that interrupt actually look like? What do people want when they do this? And I was thinking about the next set of improvements we're going to ship, and the first thing that I thought was, let's ship a bunch of knobs. To me, it was what I was hearing people wanted, they want knobs, they want sliders, they want text boxes. But then when I looked at the mocks, I was like, oh, this is great. This doesn't feel magical. It almost doesn't feel like the same thing that we've shipped so far. And so for me, I'm actually taking a little bit of time to think about how do we make even that thing and control experience much more magical and delightful.

Lenny Rachitsky (00:30:10):
Interesting. So yeah, the knobs I imagine are just like go deeper, be happier, get more serious. Yeah, because right now it's like a one shot. Here's my doc, here's the one podcast episode you get. It's the only version you can have.

Raiza Martin (00:30:27):
Yeah, yeah. And I think it's funny because I was like, the knobs seemed really apparent and I was like, is that it? Is that what people want?

Lenny Rachitsky (00:30:32):
I love that. I love that approach. I'm excited to see where you go with it. What I especially love about this vision you're describing, it super resonates with this insight I've had. So I've had a newsletter and then I had just a podcast that's just audio, and then I added video and I realized that there's just people that I just want to watch stuff and there's people that I just want to listen to stuff and then there's people I just want to read. I don't want this podcast, just shut up. I want to read it. And basically what you're describing is, well, here's information and we can deliver it to you in any medium you like. It could be blog posts, could be maybe a tweet, could be a podcast, could be a newsletter, blog post.

Raiza Martin (00:31:11):
Yeah. I mean that's exactly it. And I think even for myself, it depends on my mood. If I'm going on a walk, yeah, I want audio, but if I'm at work, yeah, most of the time text is good. And then it's kind of interesting to think about today the formats are not as malleable. I have to accept it in the format that you give it to me. But if I had sort of that power myself to choose, "Hey, thanks for this 100-page doc, I'm going to go ahead and turn it into an audio overview actually." It sort of shifts, I think, the dynamic between the person and the knowledge that's given to them. And there are actually many, many times that I've been given 100-page doc and I just didn't read it. So I wonder, I mean just frankly speaking, it's one of my funny stories is actually when I first joined Labs, Josh did give me a 50-page doc. He was like, "Here's what I think about this and this." It was basically his vision, and instead of reading it, I just grilled him. I was just like, Q&Aing him like a chatbot. Josh was like, "It's in the doc, Raiza." But the chat is easier, Josh.

Lenny Rachitsky (00:32:15):
That's so funny. You chatbotted him. Let's talk a little bit more about different use cases for this just so people can potentially get inspired. So it feels like the original use case was a scientific paper and it creates a podcast about it so you don't have to read this whole thing. Was that one of the original use cases or not?

Raiza Martin (00:32:33):
I think it's one of the common use cases. I think that's one of the ones where I think it's kind of interesting because it's like everybody wants to catch up on the latest on AI, we want to try to keep up to date on the published papers, but most of the time reading the paper can take time. It's dense, complex. You have to break down the concepts in it, and I think that's a highly sort of extensible use case. I would say the number one use case is actually a lot of students taking their study materials and wanting to turn it into an audio guide.

Lenny Rachitsky (00:33:08):
So two recent use cases that are hilarious/amazing, just will point to people in the show notes, just like they came to mind as you were talking. One is Andrej Karpathy, who's a leading AI thinker and big fan of what you're building. He keeps tweeting about how much he loves it all. He created this whole podcast series on History of Mysteries, I think it's called, History of Mysteries.

Raiza Martin (00:33:27):
I'm sorry, it's Histories of Mysteries.

Lenny Rachitsky (00:33:31):
Where he basically took the Wikipedia stories of all these mysteries of history and then turned it into a 10-episode podcast you could listen to on Spotify.

Raiza Martin (00:33:40):
Yeah.

Lenny Rachitsky (00:33:40):
Amazing.

Raiza Martin (00:33:42):
That was amazing. Actually when I saw it and I was like, "Wow, this by itself is a great product." And I think the original potato podcast that we had created was actually, I think it was because of the Wikipedia article of the day, it was about potatoes. And so there is something there. It's like, "Hey, if you want to learn something new today, maybe you can just listen to it on your drive to work or something."

Lenny Rachitsky (00:34:04):
Yeah, it's so good. Okay. The other one is the most funny is someone just uploaded the words poop and fart repeated for a long time, and the host just came up with really a kind of insightful analysis of it.

Raiza Martin (00:34:20):
Yeah, actually when I saw that one, I was about to go to bed and I was like, "All right, if I listen to this now," and this is a negative one, "I'm going to have to get my laptop and work because I can't sleep. If I feel like there's something here that's like we need to address right now, then I was like, "Okay, I'm just going to do it." So I listened to it and I listen to a lot of these and they always make me feel some kind of way. I laugh a little bit. There's one where it's like they make scary voices. That one was cool too. But this one was one of the ones where I genuinely was just really delighted at the output because it was so delightful. I don't know if you listened to the whole thing, but there's a segment where one of the speakers says, "Hey, it's kind of like you lean into the bizarre," or something, and they're describing walking past a shop that was full of rubber ducks wearing costumes, and they're like, "Oh yeah, it's silly, but you just want to lean into it so I walked into the store." And I was like, oh, it's a great analogy actually for sort of a document that just says poop and fart. There's something interesting here.

Lenny Rachitsky (00:35:32):
It's so good. And just their analysis of structure and patterns. I love that they have to come up with a 10-minute conversation around anything you give them. It feels a little mean, but they find a way.

Raiza Martin (00:35:43):
Yeah. It's true. I don't know if you've seen the chicken one, but it's pretty similar. Somebody uploaded, I think it's on Threads, it's a PDF that looks a lot like a research paper, but it just says chicken. The whole document says chicken. I would give it a listen. There's a funny segment where they're like, "Get this. It's a paper, a research paper that has more chicken in it than KFC." What? Pause, god, that's good. It's so good.

Lenny Rachitsky (00:36:12):
Oh my god. Okay, I could keep going about this all day, but let me come back to the team that's working on this and let's talk about Steven Johnson's role. So he's basically your peer. You two essentially lead this with the engineer, I imagine. Just like what's his role? How does this work at this point? What is the team looking... look like?

Raiza Martin (00:36:29):
It's so funny, I'm so fond of Steven and I tease him a lot that whenever people ping me and they want to have a meeting and I don't want to go to the meeting, I say, "Oh, I'm not the PM, it's Steven Johnson. Talk to that guy." And he was like, "So that's why all these people have been picking me." But kidding aside, Steven joined, I was like, well, this is super interesting. This has never happened to me before. There's this very accomplished, distinguished person that I really respect, love his books, love his writing, and now he's going to come work with me in a capacity where I was like, I'm just not sure what he's going to do here. But the thing about Steven is he is the most curious, most respectful, and really just full of ideas kind of person. And so when Steven joined, a lot of what was really interesting to me is I would watch how he worked, the way that he thought about language, the way that he thought about information, the way that he thinks about knowledge and sharing that with others. Because Steven's books are really incredible. It's like part mystery, super science. It's just very cool. And I was watching the way that he works and he does all of this research, and I thought, maybe this is the nugget, right? Maybe I watch Steven and I look at the way that he does these things and I look at how much time it takes for him to do it, and then I make it my own metric to crunch that down, to bring that expertise to everyday people who are not Steven Johnson. And so I learned a lot just from watching Steven, of his craft and thinking about, okay, how do I make people really, really good at de-densifying information? Because that's something we all do every day, in our own little ways. Maybe not in a Steven Johnson way. But from the get-go, I told him this. I was like, "Steven, I think you are the product. I think it's you. I'm going to follow you around. I'm going to watch everything that you do and we're going to try to figure out how we use technology to build it." And he always laughs about this, and it's really funny because he does have some very interesting workflows that I'm like, I do not see any person ever doing anything like this. He always talks about his Readwise with his 8,000 quotes or something. I'm like, that's extreme. That's crazy. I have post-its that sometimes they're crumpled in my pocket. This is the average normie flow. And what I learned from Steven is like, hey, there's something powerful about doing that, thinking about this person who has a super flow and trying to bring that to people. And so Steven is also just such a great partner with ideas. I always tell him ideas and I'm like, "Hey, crazy idea of the day." And he'll just banter with you and he'll be like, "Well, what about this? How can people do this?" And so it feels really incredible to have them on the team.

Lenny Rachitsky (00:39:25):
Is there any lessons here for how you think you'll want to build product in the future or how teams might find their own Steven for building their own product? Or is this kind of a unique case you think?

Raiza Martin (00:39:37):
I mean, it's just crazy to think that you could sort of invite someone like Steven become part of your team and have him sit with you every day and have him answer your questions about how he does things right. But I'll say that the broader lesson there for me, and it's something we've tried to live by every day, is really the how do you get users or people and really sit with them for meaningful periods of time? Because I think that has been so crucial for me, and not even just for Steven, but even with students, just follow students around, watch them do homework, watch them study, talk to them about how they feel when they study. I think just being able to do that at a really regular and intentional capacity makes a huge difference in terms of the product insights you'll come up with.

Lenny Rachitsky (00:40:25):
Can you just give a brief bio of Steven for folks that are like, who are you even talking about? I probably should have done that before I asked this question, but just like what's the TL;DR of who Steven Johnson is?

Raiza Martin (00:40:36):
Yes. Oh, I think Steven is... aside from one of the smartest people you'll ever meet, he has written 14 books, he's a New York Times bestselling author and speaker. He has a show on PBS, I can't remember what it's called, but it's on YouTube, it is really incredible, and he is a journalist. Actually, funny story about Steven is when I was about to join Labs, I really wanted to join Labs because I wanted to join Josh and whatever he was building, Josh told me, "Hey, to give you an idea of what we're doing here," he sent me a couple of things to read. And one of them actually ended up being Steven's article that he wrote, the one about how AI is mastering language, should we trust what it says, the New York Times piece. And I remember reading it and being like, yes, this is the thing. I'm going to work on it. And so before Steven had even joined, this was actually the piece that I was like, I want to go do that. I'm going to go do that in Labs. And then he ended up joining and it was just the craziest thing.

Lenny Rachitsky (00:41:36):
That's so interesting. I imagine many PMs would be like, "I don't need someone on my team that isn't building or coding or product managing or designing, just this other chef in my kitchen. Like no." And I love this actually worked out really well. It feels like he's a perfect combination of very smart future thinking, insightful, plus he's almost a model for what you want people to be able to work like.

Raiza Martin (00:41:57):
Yes. Although I will say, to be very fair, I mean Steven and I also disagree on a lot of different things. We've clashed a bunch and I think this is where I feel really grateful to have had the opportunity to work with him and to really grow with him in that way. And I used to make fun of him and I was like, "Have you ever had a coworker before Steven? Because I think you've been an author forever." And it's really funny because he's so down to earth and he's so humble that even with our disagreements, we always reach, at the end we're always aligned. Even if we don't agree about something, we're aligned on the next step. And that's really powerful I think particularly for product professionals, right, for PMs where it's like, I don't want to disagree at the end and then not have an outcome on top.

Lenny Rachitsky (00:42:49):
I love that. Okay, I have just a few more questions. I know you have to get back to work to building this thing. One is there was this hilarious moment of where the hosts basically realized, they're like, "We are AI people, and I'm scared, what's happening? I tried to call my wife and she didn't answer." Talk about that, and I want to extend to just like red teaming this thing. How do you red team this thing and make sure it's not doing things that are bad for the world, bad for Google, bad for the product?

Raiza Martin (00:43:21):
Yeah, yeah. It's such a good question. I heard that, it was over the weekend, I think it was on a Saturday or Sunday, and I remember hearing it and thinking, oh my goodness, this is actually one of those moments where you feel like we're at a fork in the road. And I hadn't read any of the comments, I just heard the audio. I think I saw it on Reddit first, and then I saw it blowing up on Twitter, and I remember thinking, what is the attitude of the world now? How do we feel about this type of audio? It was really the first thing that I thought. And so I actually spent most of that morning reading the comments, reading on Twitter. I was thinking about what is the right thing to do? Should we say something? Should we not say something? And I basically just went with what I thought was the right thing to do, which is I think people are getting to experience this technology for the first time ever. And of course, they're going to try to do things that are maybe something that we didn't think about, we didn't think they would do, or we didn't think that they could do with the jailbreaks and stuff. But I think that's such a natural part of human curiosity, and I think there was a moment where it's like, oh, do we pull this back? Because this is like, oh, is this a safe thing? But because the response I think was that people were like, "Oh, it's saying that because of the sources, this is no AI realized they were alive or something. It's actually that it was in the show notes. They were supposed to act this out." And so I felt really much more confident that like, oh, people get it, right? That's exactly what this is. Somebody uploaded some notes and said, "Hey, this is the end of the show, so make sure that you act accordingly." And that for me was enough for me to be able to say, okay, I'm going to address this publicly and say something on Twitter and make sure that people know that, hey, I've seen it and I get it. This is what people do with it. In terms of red teaming at Google though, what I'll say is this is one of the things that we care about the most. We have huge teams that work on red teaming it. We test for about as many areas as you can think of that we imagine we need to do in order to make it safe. And I think certainly, I think we'll run into situations where we didn't think about that or we haven't tested that to the fullest extent and we just add it to the test cases. I think if there was ever a scenario where we're like, "Oh, this feels pretty unsafe," we would pull it back, but I think hopefully we've built it in such a way where we don't have to do it.

Lenny Rachitsky (00:45:58):
Awesome. Yeah, I love people are just looking for ways to make it do stuff that feels wrong when it's just like, hey, we're just summarizing a thing for you in a really delightful way. Where do things go from here? We talked about it a bit. It sounds like maybe there's a mobile app in the works, there's maybe non-knobby knobs that you're working on to give people more power. For folks that are just excited about using this, where's it going? Who are you aiming to build for? Just what should people know about the future of NotebookLM?

Raiza Martin (00:46:26):
If there's one thing I could say is that we are continuing to learn from users every day, so please keep using it. Please keep sharing your feedback, whether it's on X or on Discord. I'm there every day. Even if I don't respond, I've read everything. And I say this in the most non-creepy way possible, but I say this because we are just very passionate about trying to build the right thing, the best thing for everybody. Kind of going back to sort of, hey, who are you building for? I think that there's a lot of fun use cases, but there's a lot of actually very useful game-changing workflows in here, and so we'll continue to build in that direction. I think particularly for educators, for learners, for professionals, knowledge workers, as we call them, I think there's a lot there that we'll be able to execute against in the very short term.

Lenny Rachitsky (00:47:17):
Amazing. Okay. Two final questions. If folks want to give you feedback, reach out, what's the best way to do that? Is it DM you? Is it an email, something else?

Raiza Martin (00:47:27):
Yeah, I mean, Discord. Join our Discord server. Chime in. Yeah, we're there. You can add me or yeah, X also, it's pretty good. I just came back to it and I kind of feel like I don't really know how it works now, so just a warning in case you DM me, I might just not know how it works.

Lenny Rachitsky (00:47:43):
On Twitter you mean specifically?

Raiza Martin (00:47:44):
On Twitter, on twitter, exactly.

Lenny Rachitsky (00:47:46):
And then final question, how can listeners be useful to you?

Raiza Martin (00:47:48):
I mean, please keep trying it. Try it, share your feedback, whether you find it useful, not useful, you think it's annoying, tell me. These are the things that I've heard for the last year that's helped me to make it better. So if you're inclined, please go ahead, try it, notebooklm.google.com.

Lenny Rachitsky (00:48:05):
Building an amazing product that is extremely delightful. It's one of the most interesting things on the internet today, which is a very high bar, and you've done it, and I'm really excited to see where it goes. I'm going to keep playing with it. I've been using it from my newsletter in a really fun way, and so great work and keep it up and we'll see where things go. Thanks for coming on. I know you have a lot of work to do.

Raiza Martin (00:48:26):
Oh, that's amazing. Thank you, Lenny. Thanks for having me, and thanks so much for your curiosity about it.

Lenny Rachitsky (00:48:31):
Stay curious. Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.
