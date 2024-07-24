import os
import tempfile
import streamlit as st
from streamlit_chat import message
from rag import KeplerChat


st.set_page_config(page_title="Kepler Chatbot", layout='wide')

def chat_page():

    st.image('resources/kepler_logo.png', width=700)
    st.subheader("Meet Johannes - the Kepler AI Chatbot*")
    st.write("")

    col1, col2 = st.columns([1, 3])

    # Add image to the first column
    with col1:
        st.image('resources/johannes_kepler_thuglife.png', width=200)

    # Add text to the second column
    with col2:
        st.markdown("##### Our AI assistant, Johannes, is designed to assist you with your queries regarding Kepler's curriculum.")
        st.markdown("##### He is quite the wordsmith, but please make sure you are explicit with your questions to help him help you.")
        st.markdown("##### Johannes is an intelligent assistant capable of providing interactive conversation and real-time information to help you understand more about our offerings.")
        st.write("")
        st.write("*To be specific, a 'conversational Classical Christian curriculum chat companion' that (who?) loves alliteration, wherever it (he?) can find it.")

    st.write("")
    st.write("")

    def display_messages():
        for i, (msg, is_user) in enumerate(st.session_state["messages"]):
            message(msg, is_user=is_user, key=str(i))
        st.session_state["thinking_spinner"] = st.empty()


    def process_input():
        if st.session_state["user_input"] and len(st.session_state["user_input"].strip()) > 0:
            user_text = st.session_state["user_input"].strip()
            with st.session_state["thinking_spinner"], st.spinner("Thinking..."):
                agent_text = st.session_state["assistant"].ask(user_text)

            st.session_state["messages"].append((user_text, True))
            st.session_state["messages"].append((agent_text, False))


    if len(st.session_state) == 0:
        st.session_state["messages"] = []
        st.session_state["assistant"] = KeplerChat()

        with st.spinner(f"Ingesting data."):
            st.session_state["assistant"].ingest()

        st.session_state["messages"].append(("Welcome to Kepler Education! My name is Johannes, and I will be your curriculum guide. How may I be of assistance?", False))
        
    display_messages()
    st.text_input("Message", key="user_input", on_change=process_input)

def about_page():
    st.video("https://www.youtube.com/watch?v=of3HDpZwrmM&t=72s")
    st.markdown("## What is Kepler Education?")
    st.markdown("#### Kepler is a marketplace for live, online, Classical Christian education.")
    st.write("Explore the marketplace, join the community, and find courses to prepare you or your children to honour God, live well, and do good in our complex world.")
    st.markdown("#### With Kepler, enjoy the freedom of homeschooling with the expertise of a faculty.")
    st.write("A myriad of choices (100+ courses either à la carte or on the Kepler diploma track) are available to help you achieve your child’s (or your own) educational goals.")
    st.markdown("#### Kepler can serve your family’s educational needs in additional ways.")
    st.write("Kepler also offers dual enrollment, parent commissions of desired classes, adult learning and teacher certification options, and transcript assistance.")
    st.markdown("#### Kepler connects learners from across the globe and builds genuine community.")
    st.write("Don't forget about Kepler Life, where students enrolled in Kepler courses are able to connect with each other through teacher-mentored services, real-world events, clubs, and professional development activities.")
    st.markdown("## Classical Christian Education")
    st.write("""
    Classical Christian Education is the historic liberal arts tradition which cultivates free human beings and stands in opposition to the modern progressivists’ pedagogy designed to train compliant citizens who serve as consumers and cogs in an industrialized State.
    At Kepler, we take the position that a truly Classical Christian Education is one that strives to glean the best of Western liberal arts education in every epoch. For this reason, Kepler teachers strive to foster conversation and dialogue in the true spirit of the academy where the free exchange of ideas offered respectfully and in good taste are welcome and put forth for the students' consideration and contemplation.
    """)
    st.markdown("## Kepler’s Philosophy of Education")
    st.write("""
    In short, instead of offering families another online school which limits their educational agency, Kepler offers families a way to connect with great classical Christian teachers so they can choose the best available options for their child.
    The longer version is Kepler combines the firm biblical conviction that parents are the primary educators (Ephesian 6:4) with a strong desire to equip and support parents in their God-ordained task. Therefore, Kepler exists to make a Classical Christian Education available, affordable, and accessible to everyone who wants to possess such an education.
    """)
    st.markdown("#### Available")
    st.write("""
    What is called Classical Christian Education today used to be called a liberal arts education. But like many words in a dynamic language, liberal arts education doesn't mean what it used to. A historic liberal arts education was the education of the free man, one who both ruled himself well but also influenced and ruled society well (thus, liberal from the Latin liberalis meaning free). Kepler makes what was once considered an elite education available to everyone who wants the liberating education of a free person.
    """)
    st.markdown("#### Affordable")
    st.write("""
    Given that Kepler is an online platform—a consortium of independent highly-qualified teachers—and not a school, the Kepler model removes the bureaucracy and administrative costs and brings committed Classical Christian educators and families together. Kepler ensures Classical Christian Education is affordable by employing marketplace dynamics. At Kepler, vetted and qualified teachers set their own prices and schedules, and parents choose the right teachers and courses for their children. Kepler is, in essence, a free-market platform for Classical Christian Education.
    """)
    st.markdown("#### Accessible")
    st.write("""
    Kepler leverages the best available technology to provide a teaching platform and community that attracts the best teachers in their field; thereby, Kepler makes Classical Christian Education not only available and affordable, but also accessible. Any student with a reliable internet connection and well-functioning computer can access some of the best classical Christian educators in the world from anywhere in the world.
    Learn more from our short film, "We've Been Schooled!, at the top of the page.
    """)
    st.markdown("## University Model Courses")
    st.write("""
    Kepler uses a “flipped classroom” or “university model” approach, where students read assigned material, watch pre-recorded lectures, and complete written assignments asynchronously throughout the week. 
    The class then meets with their instructor online for about 90 minutes once per week to have Socratic dialogues or recitations. 
    Students actually spend less time in the classroom or in front of a computer screen and more time actually learning from the great tutors like Plato, Aristotle, Edmund Burke, and C. S. Lewis.
    """)
    st.markdown("## Core Values & Quality Control")
    st.write("""
    All Kepler teachers are vetted by way of written and verbal interviews, third-party criminal background checks, and when necessary, by transcript and teaching experience reviews. We ensure every teacher on the Kepler platform is qualified to teach and ascribes to the Christian faith, classical pedagogy, and maintains a conservative worldview.
    """)
    st.markdown("#### Mere Christian")
    st.write("""
    Kepler teachers embrace those essential, common, and core beliefs left by Christ and the Apostles to the church catholic, the body of Jesus Christ on Earth, held through the ages by all orthodox Christian traditions alike. All Kepler teachers affirm the Nicene Creed as a minimum statement of their faith. Specific details of each teacher's statement of faith can be found on his or her teacher profile.
    """)
    st.markdown("#### Broadly Classical")
    st.write("""
    While it must be recognized that this great tradition of Classical Christian Education is mildly dynamic, developing over more than two millennia of Western civilization and expresses itself under a fairly broad tent of thought, Kepler teachers share a commitment to the Great Books of the Western tradition and engage students in the pursuit and acquisition of the liberal arts, that knowledge which is pleasurable for its own sake, and which frees the mind and prepares the soul to be wise and virtuous.
    """)
    st.markdown("#### Historically Conservative")
    st.write("""
    Kepler teachers recognize, value, and delight in the permanent things and believe the necessary and healthy pursuit of cultural reformation must accord with the contours of Scripture, natural law, and the created order. Kepler teachers strive to cultivate the same in their students.
    """)
    st.markdown("## Why Kepler?")
    st.write("""
    Kepler is inspired by the early modern scholar, Johannes Kepler, widely known for his commitment to Christ, the liberal arts, and the advancement of science in the West. While modern education argues over the value of STEM vs. Liberal Arts, men like Kepler embraced and advanced the integration of knowledge as essential to being an educated person. 
    As Kepler seeks to champion this same integrated approach to learning, Johannes Kepler accurately exemplifies the courageous, innovative, and robust intellectual approach to education and human flourishing needed in the modern age. We are humbly attempting to cultivate such a spirit within Kepler's academic consortium.
    """)


def kepler_classical_christian_page():
    st.image('resources/liberal_arts_image.webp', width=800)
    st.title("What is Classical Christian education?")
    st.write("""
    >"The Kepler Classical Christian Curriculum is rooted in the rich tradition of classical education. It emphasizes the development of critical thinking skills, a deep understanding of classical literature, history, and philosophy, and the integration of a Christian worldview into all areas of study. Our curriculum is designed to cultivate wisdom and virtue by nourishing the soul on truth, goodness, and beauty.

    ## **What is Classical Christian Education?**
             
    Classical Christian Education is the approach to education that was both taken up by free human beings and that which cultivated free human beings within Western civilization for the past three millennia. Expressed under a fairly broad tent of thought, there are likely as many micro-persuasions as there are eyes on Argos, which is true for at least three reasons.

    First, what we call Classical Christian Education today has looked differently throughout various epochs of history. Depending on who is answering the question, “What is Classical Christian Education?,” one may get a slightly different answer if they are focusing on pre-Christian classical education, or classical education as it functioned during the Scholastic period, the Renaissance period, the modern period of classical Christian renewal that began in the early 1980s, or what some are now calling Christian Classical Education.

    The second reason is during this modern age of recovering Classical Christian Education, educators have continued to grow in their understanding of what Classical Christian Education is. For example, in The Liberal Arts Tradition, written by Kevin Clark and Ravi Jain, the authors suggest there have been four periods of growth in the Classical Christian Education movement.

    The third reason is directly related to the first two. As understanding has grown about what Classical Christian Education has been and how it was implemented in ages past, so have opinions about which historical expression is most important to recover in the modern world (i.e., do students in the modern world still need to study Latin to be classically educated? Wouldn’t studying modern languages do just as well?) Also, where does the study of more specialized sciences like, biology and ecology, fit into Classical Christian Education?

    In a nutshell, while Classical Christian Education is a historic tradition of education that stands in opposition to the modern progressivists’ pedagogy and agenda, it must be recognized that this great tradition is mildly dynamic, developing over more than two millennia of Western civilization.

    At Kepler, we take the position that a truly Classical Christian Education is one that strives to glean the best of Western liberal Education in every epoch. Therefore, Kepler teachers strive to foster conversation and dialogue in the true spirit of the academy where the free exchange of ideas offered respectfully and in good taste are welcome and put forth for the students' consideration and contemplation.

    **How is Classical Christian Education defined?**
                
    The Association of Classical Christian Schools provides one of the most concise definitions of Classical Christian Education:

    > Classical Christian education (CCE) is a time-tested educational system which establishes a biblical worldview (called Paideia), incorporates methods based on natural phases of student development, cultivates the seven Christian Virtues, trains student reasoning through the Trivium (Grammar, Logic, and Rhetoric), and interacts with the historical Great Books.

    The ['Well Trained Mind'](welltrainedmind.com) website gives a far more expansive definition, then summarizes it this way:

    > A classical education, then, has two important as- pects. It is language-focused. And it follows a specif- ic three-part pattern: the mind must be first supplied with facts and images, then given the logical tools for organization of facts, and finally equipped to express conclusions.

    While these definitions are both accurate and sound as far as they go, neither mention an essential aspect of Classical Christian Education, the subjects treated in the Quadrivium, the second half of the seven liberal arts; further, what is accurately mentioned still requires some unpacking to more fully answer the question, What is Classical Christian Education?

    At Kepler, we consider these following seven characteristics that are shared by all expressions to be fundamental to Classical Christian Education:

    **Characteristic 1**
                
    The first characteristic of a Classical Christian Education is the development and cultivation of Paideia, a word whose etymology can be recognized in words like pediatrics or pedagogy. In his letter to the saints at Ephesus, St. Paul writes,

    “Fathers, do not provoke your children to anger, but bring them up in the discipline and instruction of the Lord” (Ephesians 6:4, ESV).

    The word translated discipline here is the Greek word, paideia, and is defined as the act of providing guidance for responsible living . . . upbringing, training, instruction . . . chiefly as it is attained by discipline, correction.[^1] Paideia is very much related to the word translated discipline in this verse, the Greek word nouthesia. It means counsel about avoidance or cessation of an improper course of conduct, admonition.[^2]

    Definitions are noted here to draw attention not only to the denotation of paideia but also to its connotation. It reveals the fundamental nature of education, the rearing of a young person in a proper view of the world; that is, a worldview that guides the way he should go (Proverbs 22:6).

    While the word worldview brings its own set of baggage to the conversation, it is used here to mean thinking Christianly about the world in which we live and move and have our being.

    A young person with a Christian worldview possesses a comprehensive vision of the cosmos as having been created and (still) being redeemed by God. He or she also possesses a moral imagination informed first by the truth of Scripture, but also by the noble traditions of the Church. This idea of Christian worldview falls into the stage of education that will later be addressed as piety.

    **Characteristic 2**
                
    The second characteristic of a Classical Christian Education is its focus on a liberal or humane education. In opposition to the modern and slavish approach to training mere workers for an institutionalized and crony-capitalist society, Classical Christian Education seeks to educate the whole person, human qua human. This is to what liberal (libere) in the liberal arts refers; a Classical Christian Education is the education of a liberated person, or the education that makes for a full and free human being.

    Regarding education oriented to job training in a world where vocations ebb and flow like the tide, consider the words of John W. Gardner, author of Excellence, who rightly noted,

    > “We don’t even know what skills may be needed in the years ahead. That is why we must train our young people in the fundamental fields of knowledge, and equip them to understand and cope with change. That is why we must give them the critical qualities of mind and durable qualities of character that will serve them in circumstances we cannot now even predict.”[^3]

    The ability to rightly cope with change can only be accomplished by receiving a liberal arts education. John of Salisbury, the secretary and counselor to the renowned Archbishop of Canterbury, Thomas Becket, also asserted a similar proposition in his influential treatise on education, Metalogicon. Published in 1159, John of Salisbury recognized the ability of the liberal arts to cultivate imaginative and wise autodidactics. He wrote,

    > “The liberal arts are said to have become so efficacious among our ancestors, who studied them diligently, that they enabled them to comprehend everything they read, elevated their understanding to all things, and empowered them to cut through the knots of all problems possible of solution.”[^4]

    And to the point of the importance of educating the whole person, Robert Maynard Hutchins notably concurred when he wrote,

    > “Nobody can decide for himself whether he is going to be a human being. The only question open to him is whether he will be an ignorant undeveloped one or one who has sought to reach the highest point he is capable of attaining.”[^5]

    **Characteristic 3**
                
    The third characteristic of Classical Christian Education is a pedagogical method that follows the order of the medieval seven liberal arts, mainly as it relates to a child’s development but also as an approach to teaching all subject matter. The seven liberal arts are described by the medieval divines as the trivium (three ways) and the quadrivium (four ways).

    First, following the trivium, students learn grammar (language), then dialectic (logical thinking), and finally rhetoric (expressing oneself accurately and persuasively) before moving on to studying the quadrivium. The quadrivium treats four universal truths: number, geometry, harmony, and astronomy.

    Early in the modern renewal of Classical Christian Education, those seeking to recover the classical model of education relied on an essay by Dorothy Sayers, titled, “The Lost Tools of Learning.” It was an extremely helpful essay and many schools adopted her pedagogical model. But the recovery didn’t stop there.

    In the midst of “repairing the ruins,” more about classical pedagogy was discovered. Sayers’ pedagogical insights were just the tip of the iceberg, to lean on a worn-out metaphor. Recovery of classical pedagogy also revealed just how important poetic knowledge was to the formation of the whole person.[^6]

    Today, most recognize a much fuller expression of Classical Christian Education that was first laid out by Ms. Sayers. Referred to by Clark and Jain as the PGMAPT paradigm (i.e., piety, gymnasium, music, liberal arts, philoso- phy, and theology), where the A stands for the liberal arts (trivium and quadrivium), and the seven liberal arts are bookended by poetic knowledge on one end and modern consummate studies on the other.

    **Characteristic 4**
                
    The fourth characteristic recognizes the pedagogical approach must be applied to something. In other words, Classical Christian Education is more than a pedagogy, it is a pedagogy applied to a specific pool of knowledge, the best of what has been thought and written in the last two- and-a-half millennia of the Western tradition.

    Sometimes this pool or “Western canon” of knowledge is referred to as the Great Books. When referring to great books, some may immediately recall Mortimer J. Adler’s 60-volume set published by the University of Chicago and Encyclopedia Britannica. His are merely a collection of the kinds of works to which the Great Books refer. While it is a good collection, it is also an incomplete collection.

    The president of Harvard College, Charles Eliot, suggested his own list of similar books which affectionately came to be called his “five-foot shelf” and published as The Harvard Classics.

    Classical Christian Education makes a point of exposing students to these primary sources in an integrated fashion, finding in both the classical and Christian traditions that all truth (i.e., reality) is part of the whole. In other words, knowledge of any subject is only a partial knowledge of the one Truth.

    Instead of studying textbooks of disintegrated subjects, students of a Classical Christian Education often study the humanities in a more integrated manner. This means they read and discuss in Socratic fashion the best primary literature, philosophy, theology, and history, often within a given historical period.

    **Characteristic 5**
                
    The fifth characteristic of Classical Christian Education is the study of classical languages, including Greek, and especially Latin. While a few have made a somewhat meritorious argument of substituting Latin with modern languages, there are many stronger arguments for the continued inclusion of classical languages in a Classical Christian Education. A few of those arguments are:

    - Learning Latin gives students the ability to read many important primary sources in Latin, the language in which they were written; it also affords opportunity to read texts that have not yet been translated into English.
    - Learning Latin provides students with a fuller understanding of the English language since about 40 percent of English is derived from Latin.
    - Many of the professional vocations still do—and probably always will—rely heavily on Latin languages (e.g., law, science, medicine, theology).
    - And one ancillary and pragmatic reason is that students who study Latin overwhelmingly score higher on standardized tests than students without this near-magic ability.

    In any case, Classical Christian Education emphasizes the learning of not only modern languages but the classical languages as a fundamental staple of a human beings education.

    **Characteristic 6**
                
    The sixth element is teaching students with the goal of fostering virtue and wisdom instead of helping them merely accumulate disconnected facts or skills for the job market. While modern education takes what it claims to be a secular approach, wrongly believing education can only consist of the is and not the ought, Classical Christian Education emphasizes what a student ought to be, virtuous, by highlighting what David Hicks, in his book, Norms and Nobility, calls the “Tyranny of the Ideal Image.”

    This Ideal Image is exemplified by the seven Christian virtues (i.e., prudence, fortitude, wisdom, justice, faith, hope, and love) and also as revealed in the person of Jesus Christ (Ephesians 4:11-16).

    **Characteristic 7**
                
    The seventh characteristic has already been alluded to in relation to at least two other characteristics, namely in that students read primary sources and classical languages are essential. However, it would be remiss not to emphasize the fact that Classical Christian Education is language-fo-cused learning rather than image-focused learning. This does not mean Classical Christian Education excludes the plastic arts (i.e., painting, sculpting, etc.); quite the contrary. It simply means it emphasizes language-based learning.

    In other words, Classical Christian Education emphasizes learning through words, written and spoken, rather than through videos or other types of imaging. This short excerpt from Dorothy Sayers’s essay, “Lost Tools of Learning” is just as apropos to the entire enterprise of recovering Classical Christian Education in a world dominated by pixels as it is to this seventh characteristic. Sayers writes,

    > By teaching them all to read, we have left them at the mercy of the printed word. By the invention of the film and the radio, we have made certain that no aversion to reading shall secure them from the incessant battery of words, words, words. They do not know what the words mean; they do not know how to ward them off or blunt their edge or fling them back; they are a prey to words in their emotions instead of being the masters of them in their intellects. We who were scandalized in 1940 when men were sent to fight armored tanks with rifles, are not scandalized when young men and women are sent into the world to fight massed propaganda with a smattering of “subjects”; and when whole classes and whole nations become hypnotized by the arts of the spellbinder, we have the impudence to be astonished. We dole out lip-service to the importance of education—lip-service and, just occasionally, a little grant of money; we post-pone the school—leaving age, and plan to build bigger and better schools; the teachers slave conscientiously in and out of school hours; and yet, as I believe, all this devoted effort is largely frustrated, because we have lost the tools of learning, and in their absence can only make a botched and piecemeal job of it.
    """)

st.sidebar.title("Explore Kepler")
page = st.sidebar.radio("Go to", ["Kepler Chatbot", "About Kepler Education", "Classical & Christian"])

if page == "Kepler Chatbot":
    chat_page()
elif page == "About Kepler Education":
    about_page()
elif page == "Classical & Christian":
    kepler_classical_christian_page()

if __name__ == "__main__":
    pass