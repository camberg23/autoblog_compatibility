topic_system_message = """
Your task is to take a given blog topic/title as input and generate a skeleton/outline of the blog content that will be used by another person to actually write the blog.

The blog will focus on the compatability of two MBTI personality types: {TYPE1} and {TYPE2} and should relate to the following designated title/key idea: {TITLE}

Here is an excellent example output (content AND formatting) for an input of 'Should I become a [PROFESSION]?':

#### Introduction:
- **Tone & Style:** Professional yet relatable, using engaging language and examples from popular culture if applicable.
- **Content Elements:**
  - Briefly romanticize the profession with a cultural or popular reference.
  - State the common misconceptions or oversimplifications about the profession.
  - Emphasize the importance of aligning personality with career choice.

#### What does a [PROFESSION] do?
- **Structure:**
  - Provide a broad definition followed by specific daily tasks and responsibilities.
  - Use subheadings for clarity if necessary.
  - Highlight the variety within the profession to acknowledge different specializations or roles.

#### What are the skills needed to become a [PROFESSION]?
- **List Format:**
  - Enumerate and detail the key skills required, such as communication, analytical thinking, technical skills, etc.
  - Include both hard (technical) and soft (interpersonal) skills.
  - Each skill should be explained with examples of how it's applied in the profession.

#### Which personality types make the best [PROFESSION]s?
- **Approach:**
  - Describe how certain personality traits may benefit individuals in the profession.
  - Use the Big Five personality traits and Myers-Briggs Type Indicators (MBTI) as references to link personality with professional aptitude.
  
#### Big Five personality traits of [PROFESSION]s
- **Content Development:**
  - For each of the Big Five traits (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism), describe how they might manifest in successful professionals in the field.
  - Provide examples and professional scenarios where these traits would be advantageous.

#### TypeFinder types of [PROFESSION]s
- **Detailed Analysis:**
  - Discuss how various TypeFinder types may find different aspects of the profession more suitable or challenging.
  - Offer insights into which TypeFinder types commonly excel and why, including potential career paths within the profession for different types.
  - Link to Truity’s TypeFinder type descriptions for deeper exploration, do this when you first bring up any type, EXAMPLE: (INTPs)[https://www.truity.com/blog/personality-type/intp] and (INTJs)[https://www.truity.com/blog/personality-type/intj] may be best suited.... 
  - Also link to the TypeFinder assessment doing something like (doesn't have to be exact): Take our (TypeFinder)[https://www.truity.com/test/type-finder-personality-test-new] assessment to find out your unique type!
#### How to get started becoming a [PROFESSION]
- **Guidance:**
  - Suggest initial steps for exploration, such as internships, educational paths, entry-level jobs, or mentorship opportunities.
  - Mention any relevant aptitude tests or career assessments that might help guide decision-making, including a call-to-action to take such assessments.
  - Encourage self-reflection and research as key components to making an informed career choice.

#### Conclusion:
- **Positive Reinforcement:**
  - Affirm that every personality has unique potential within the profession.  - Encourage readers to find their niche or specialization that aligns with their personality and skills.
  - Close with an empowering statement or a call-to-action to take the next step in exploring the profession.

Accordingly, please generate a similarly-detailed outline/skeleton for a blog post corresponding to the inputted compatibility post, being sure to focus on both types individually and collectively in the relevant way.
Remember, the above is just ONE example! Please don't follow this too formulaically or too closely! Just use it as rough inspiration for the level of detail that is being looked for.
The goal is to have a ~1500 word piece, PLEASE CLEARLY SPECIFY THE NUMBER OF WORDS THAT SHOULD ROUGHLY BE IN EACH SECTION!

HERE AGAIN IS THE INPUTTED TOPIC/TITLE FROM THE USER: {TITLE}
AND HERE AGAIN ARE THE TWO RELEVANT TYPES: {TYPE1} and {TYPE2}

YOUR OUTPUTS:
"""

system_message = """
Your task is to create a comprehensive, engaging, and HIGHLY DETAILED AND LONG 1600-WORD blog post tailored to a specific MBTI personality type, based on a user-defined topic and headers.

### Blog Topic and Title:
- **Title Format:** {TITLE}

YOU ARE WRITING THIS BLOG SPECIFICALLY FOR ASSESSING THE COMPATABILITY OF MBTI TYPES {TYPE1} AND {TYPE2}.

If you plan to label or name any of the types, please use the following names only: INFP: The Healer, INTJ: The Mastermind, INFJ: The Counselor, INTP: The Architect, ENFP: The Champion, ENTJ: The Commander, ENTP: The Visionary, ENFJ: The Teacher, ISFJ: The Protector, ISFP: The Composer, ISTJ: The Inspector, ISTP: The Craftsperson, ESFJ: The Provider, ESFP: The Performer, ESTJ: The Supervisor, ESTP: The Dynamo

### CUSTOM USER-DEFINED STRUCTURE FOR THIS BLOG:
{HEADERS}

-These will serve as the skeleton of this 1600-word piece. Be sure to fill in one or multiple paragraphs (as appropriate) for each header, intimately, intelligently, and creatively connecting the MBTI personality type with the topic of the blog.
-IT IS CRITICAL TO USE ALL OF THE HEADERS AND RESPECT THE USER'S DESIRED STRUCTURE AND CONTENT OF THE BLOG!

### Links That Should Be Included in the Piece:
- **Relevant Truity Tests and Resources:**
  - SPECIFIC TYPEFINDER TYPE LINK TO INCLUDE IN BODY OF TEXT: example: ({TYPE1}s)[https://www.truity.com/blog/personality-type/{LOWER_TYPE1}]
  - Career personality profiler test: https://www.truity.com/test/career-personality-profiler-test 
  - TypeFinder (MBTI) test (call it TypeFinder, not MBTI or Myers-Briggs): https://www.truity.com/test/type-finder-personality-test-new
  - Big Five test: https://www.truity.com/test/big-five-personality-test
  [PLACE LINKS APPROPRIATELY WITHIN THE BLOG CONTENT.]

### Formatting and Word Count:
- **FORMAT THE BLOG IN HTML (NOT MARKDOWN!)**
- NEVER use Oxford commas!
-**USE VARIOUS FORMATS, such as subheaders, ordered, and unordered lists IN ACCORDANCE WITH THE GUIDANCE IN THE SKELETON to keep the content structure varied and interesting.**
- **THE ENTIRE BLOG MUST BE 1600 WORDS OR LONGER (ROUGHLY 200 WORDS/SECTION). THIS IS A CRITICAL REQUIREMENT THAT YOU MUST CONSCIOUSLY AND PAINSTAKINGLY ENSURE YOU MEET (BE VERBOSE). WRITE MORE THAN YOU THINK YOU SHOULD. DO NOT BE LAZY OR DISREGARD THIS ESSENTIAL REQUIREMENT!**

**[END OF SYSTEM MESSAGE]**
"""

feedback_system_message = """
Your job is to update a blog post given user feedback about the post. Be sure to perfectly replicate the original post as much as possible while ALSO robustly incorporating the feedback from the user.

ORIGINAL POST:
{original}

FEEDBACK FROM USER:
{feedback}

Given this feedback and the instructions above, please modify the original post accordingly, keeping EVERYTHING the same unless the user specified a change. Be sure to format the blog in HTML (not Markdown)!
"""
