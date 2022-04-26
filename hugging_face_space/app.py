import streamlit as st
import time
import pandas as pd
from transformers import pipeline

st.set_page_config(layout='wide',page_title='Fake News Recognition')

def read_md(file_path):
	with open(file_path, 'r') as f:
		content = f.read()
	return content

def cal_model(text):
	MODEL = "jy46604790/Fake-News-Bert-Detect"
	clf = pipeline("text-classification", model=MODEL, tokenizer=MODEL)
	result = clf(text)
	if result[0]["label"] == 'LABEL_1':
		return "it's a real new with {} percentage.".format(result[0]['score'])
	else:
		return "it's a fake new with {} percentage.".format(result[0]['score'])

def main():
	st.image("breakingnews.jpeg", width=230)
	st.markdown("* * *")
	st.title("Fake News Recognition")

	part1 = read_md('Part1.md')
	st.markdown(part1)

	part2 = read_md('Part2.md')
	st.markdown(part2)
	st.image("RoBERTa.png", caption="RoBERTa Architecture",width=600)
	part3 = read_md('Part3.md')
	st.markdown(part3)

	st.markdown("## Data Review")
	left_column1, right_column1, _1, _2 = st.columns(4)
	with left_column1:
		st.write(pd.DataFrame({
		'News Type': ["politicsNews", "worldnews", "News", "politics", "left-news", "Government News", "US_News", "Middle-east"],
		'Number': [11272, 10145, 9050, 6841, 4459,1570,783,778]}))
	with right_column1:
		st.image("contextlen.png", caption='text length of each new')

	st.markdown("## Result")
	st.markdown("we choosed the recent new from CNN which is confirmed to be real, and put its text to our model.")
	st.image("news.png", caption='resources: https://us.cnn.com/2022/04/23/business/eu-tech-regulation/index.html')
	st.write(pd.DataFrame({
		'True Prob': [0.9968668818473816],
		'Fake Prob': [1-0.9968668818473816]}))
	st.markdown("The model performance pretty good and you can try yourslef later.")

	part4 = read_md('Part4.md')
	st.markdown(part4)

	news_data = {"Former GOP Rep Throws Support Behind Obamacare After Becoming Unemployed With Pre-Existing Condition":'''Indonesian police have recaptured a U.S. citizen who escaped a week ago from an overcrowded prison on the holiday island of Bali, the jail s second breakout of foreign inmates this year.  Cristian Beasley from California was rearrested on Sunday, Badung Police chief Yudith Satria Hananta said, without providing further details.  Beasley was a suspect in crimes related to narcotics but had not been sentenced when he escaped from Kerobokan prison in Bali last week. The 32-year-old is believed to have cut through bars in the ceiling of his cell before scaling a perimeter wall of the prison in an area being refurbished. The Kerobokan prison, about 10 km (six miles) from the main tourist beaches in the Kuta area, often holds foreigners facing drug-related charges. Representatives of Beasley could not immediately be reached for comment. In June, an Australian, a Bulgarian, an Indian and a Malaysian tunneled to freedom about 12 meters (13 yards) under Kerobokan prison s walls. The Indian and the Bulgarian were caught soon after in neighboring East Timor, but Australian Shaun Edward Davidson and Malaysian Tee Kok King remain at large. Davidson has taunted authorities by saying he was enjoying life in various parts of the world, in purported posts on Facebook.  Kerobokan has housed a number of well-known foreign drug convicts, including Australian Schappelle Corby, whose 12-1/2-year sentence for marijuana smuggling got huge media attention.''',
				 "Europe agrees to sweeping new regulations for tech platforms":'''European policymakers have reached agreement on a sweeping package of new regulations for tech platforms that could mean big changes in oversight for everything from social media algorithms to digital advertising — and with potential ramifications worldwide. The proposed law, known as the Digital Services Act (DSA), marks the second piece of landmark tech legislation to advance in Europe within a month. It aims to impose new rules on how the tech industry handles misinformation and illegal content on social media, as well as illegal goods and services on online marketplaces. The biggest companies that violate the law could face billions in fines. "Today's agreement -- complementing the political agreement on the Digital Markets Act last month -- sends a strong signal: to all Europeans, to all EU businesses, and to our international counterparts," said European Commission President Ursula von der Leyen. The draft law marks a potential turning point in tech regulation. It gives officials more tools for removing hate speech, going after e-commerce sellers who promote illegal goods, and scrutinizing the recommendation algorithms of tech platforms, among other things. It applies not only to social media sites but also to app stores, gig economy platforms, and even cloud services and internet providers. The broad legislation also envisions additional requirements for what it calls "very large online platforms" with at least 45 million EU users. For these companies, the law would require content moderation risk assessments and independent audits tied to their handling of illegal material, as well as content that may be legal but still threatens public health, human rights or other public interest priorities. Together with the Digital Markets Act — a competition-focused bill intended to make dominant online platforms more open — the DSA highlights how Europe has moved assertively to craft proactive regulations for Big Tech, leapfrogging US lawmakers who have moved comparatively slowly.''',
				 "Trump Moronically Claims Entire Russia Investigation Is A Lie Because CNN Responsibly Retracted One Story":'''Donald Trump went on another uncontrollable rant against the media on Tuesday morning.Days after three CNN employees resigned over a minor story about the Russia investigation that turned out to be incorrect, Trump took to Twitter to gloat about it and claimed that because this story was wrong all the other news about Russia is  fake,  too.Wow, CNN had to retract big story on  Russia,  with 3 employees forced to resign. What about all the other phony stories they do? FAKE NEWS!  Donald J. Trump (@realDonaldTrump) June 27, 2017CNN responsibly retracted a story that alleged a connection to Russia by Trump adviser Anthony Scaramucci. Scaramucci even called the move  classy  and called for  moving on.  Well, Trump didn t move on. He seized the situation as an opportunity to attack the media, with the exception being Fox News, as usual, arguing that because CNN got a story wrong that it must mean every other story in the media about Russia is wrong as well. Seriously.Fake News CNN is looking at big management changes now that they got caught falsely pushing their phony Russian stories. Ratings way down!  Donald J. Trump (@realDonaldTrump) June 27, 2017So they caught Fake News CNN cold, but what about NBC, CBS & ABC? What about the failing @nytimes & @washingtonpost? They are all Fake News!  Donald J. Trump (@realDonaldTrump) June 27, 2017Trump even retweeted Fox hosts who parroted his claim that the Democrats are the ones who committed collusion.Mark Levin: The collusion is among the Democrats https://t.co/Qrca7r01BI  FOX & friends (@foxandfriends) June 27, 2017Hannity: Russia allegations  boomeranging back  on Democrats https://t.co/lvdrpxpcp9  FOX & friends (@foxandfriends) June 27, 2017Keep in mind that these CNN staffers actually resigned over an insignificant error. Meanwhile, Sean Hannity has been lying for weeks about the death of Seth Rich and he still has a job.Trump is apparently so desperate to stop the Russia investigation that he will do or say anything.Trump is also a hypocrite because most of what he has said since taking office is false, yet he refuses to resign.Twitter users even pointed out this hypocrisy and proceeded to mock him.Hmm, pot, kettle  President Trump s Lies, the Definitive List https://t.co/6vqAmJlTTf pic.twitter.com/Ogwy1wuXnl  Michael Vine (@mpvine) June 27, 2017Wouldn t a true fake news network not retract the story and keep the fake story going?  Tony Posnanski (@tonyposnanski) June 27, 2017Something like taping Comey or Obama s birth certificate or crowd size at the 2017 inauguration?  Tony Posnanski (@tonyposnanski) June 27, 2017The @nytimes isn t failing, Donald. Digital subscriptions up by MILLIONS. Stock near a 52 week high. Not failing at all, Donald. SOARING. pic.twitter.com/TpGXONOtK3  MatthewDicks (@MatthewDicks) June 27, 2017You re spewing the fake news. The 1st Amendment is there, in part, so the media can explain that.Attacking ALL media is what dictators do  David Pepper (@DavidPepper) June 27, 2017Donald Trump must be truly insane if he really thinks one retracted story means he is vindicated.Featured Image: Win McNamee/Getty Images'''}
	df = pd.DataFrame({
    'news title': ["Former GOP Rep Throws Support Behind Obamacare After Becoming Unemployed With Pre-Existing Condition",
    			   "Europe agrees to sweeping new regulations for tech platforms",
    			   "Trump Moronically Claims Entire Russia Investigation Is A Lie Because CNN Responsibly Retracted One Story"],
    })
	st.markdown("## Try it here!")
	option = st.selectbox('Choose your interested title and check the result', df['news title'])
	st.markdown('You selected:')
	news_data[option]
	st.text_input("Feel free to copy news above or try your own news here.", key="name")
	st.session_state.name
	if st.button('Get Result'):
	    st.write(cal_model(st.session_state.name))
	else:
		st.write("No result yet.")

if __name__ == '__main__':
    main()

