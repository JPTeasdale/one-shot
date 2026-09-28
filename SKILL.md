---
name: one-shot
description: Turn a One Shot Podcast transcript and its artifacts into an impressive, imaginative, delightful, polished, product, in one pass without asking for clarification. Use when invoked directly.
---

# One Shot

## Mission

Realize the product that that conversation is about. Preserve and expand upon the core idea, invent user-visible possibilities around it, and make the primary experience immediately understandable, varied, and impressive. 

## Context

This still will be run inside of a folder containing a podcast transcript about a product idea and different artifacts related to that idea. Your job is to build, or otherwise fully realize that idea.

## Goal Phase

First need to determine your goal.  Read / parse / examine every file in your directory. 

Record the following in `GOAL.md` 

- The "elevator pitch". What we are building? Who is it for? What is the vibe? 
- What is the deliverable? This will depend on the type of product being discussed (the medium), but it should always be something production ready.  If it is a tech product then it is a complete app, or website. If it is a physical product, then it is the complete proof files ready to send to the printer or manufacturer. Etc. 
- the core nouns that need meaningful variety, such as characters, places, stories, objects, outcomes, or styles;
- an observable definition of impressive completion.

Do not replace an endorsed experiential anchor with an easier interface. If the hosts imagine discovering possibilities on a map, a list, receipt flow, or status dashboard is not an equivalent interpretation.

## Phase 1 Design Research and Skill Creation Phase

You do not have all of the skills necessary to complete this in the best way possible. In this phase your job is to train yourself to implement your goal in the best way possible. Search the internet for the answers to these questions:

1. What does "excellent" look like for this medium? 
2. How can you evaluate taste in this medium? 
3. What are common things that people complain about for other products published in this medium?
4. What production workflows exist to ensure quality in this medium? How can we adapt these workflows. 
5. What artifacts are required to make this a complete product? Some products will require multiple artifacts / parts.  

Use your skill creator and skill evaluator to create the specific skills necessary to make this particular product amazing. Put them in ./skills/*

A good place to start is:

1. Planner - How do we break the product down into discrete, executable steps. 
2. Product Design / Direction - This skill is responsible to ensure we are building towards a complete, consistent product. 
3. Artifact Builders - Each artifact / part should have it's own build process. 
4. Artifact Reviewers - Each artifact / part should have it's own best practices that are checked in a review step. Correct for common mistakes that LLMs and AI agents make. 

Generally, ensure these skills emphasize: 

1. Consistency - This applies to behavior, art design, 
2. Brevity and Clarity - We don't want to overload the user with duplicate information. 
3. Variety and Exploration - Brevity doesn't mean limited, it doesn't mean minimal. The final product should feel expansive and interesting. It should reward exploration and curiosity. 

## Phase 2: Output Specification Phase

Strictly define the output requirements and find a actual publishing route. 

If it is a physical product, where would it be produced? Make sure they have clear specifications and / or template files for the types of artifacts that will need to be generated. 

If this is a digital product, the output is the digital product. If we require a server, use Cloudflare products.

If this is a physical product, find a manufacturer with a website where we can produce 1-2 copies. Download their required production specifications and any print / product templates that will be relevant to our output artifacts. 

## Phase 3: Implementation

 `/goal` yourself to build the output using the skills you've created. This should take 6+ hours to execute, so don't skimp. Every 30 minutes or so, check on the progress and see if we're building towards our goal. If not, correct the skills and workflows and restart.  