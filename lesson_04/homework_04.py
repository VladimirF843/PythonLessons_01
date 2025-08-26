adwenturesadwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# task 01
str1 = adwentures_of_tom_sawer.replace("\n", " ")
print("Task 01:", str1[:50] + "...")

# task 02
str2 = str1.replace('....', ' ')
print("Task 02:", str2[:50] + "...")

# task 03
str3 = " ".join(str2.split())
print("Task 03:", str3[:50] + "...")

# task 04
h_count = str3.count('h')
print("Task 04:", h_count)

# task 05
count_upper = sum(1 for word in str3.split() if word and word[0].isupper())
print("Task 05:", count_upper)

# task 06
perviy = str3.find("Tom")
vtoroy = str3.find("Tom", perviy + 1)
print("Task 06:", vtoroy)

# task 07
adwentures_of_tom_sawer_sentences = str3.split('. ')
print("Task 07: Количество предложений:", len(adwentures_of_tom_sawer_sentences))

# task 08
if len(adwentures_of_tom_sawer_sentences) >= 4:
    fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
    print("Task 08:", fourth_sentence)
else:
    print("Task 08: Нет четвертого предложения")

# task 09
starts_with_by_the_time = any(sentence.strip().startswith("By the time")
                            for sentence in adwentures_of_tom_sawer_sentences)
print("Task 09:", starts_with_by_the_time)

# task 10
if adwentures_of_tom_sawer_sentences:
    last_sentence = adwentures_of_tom_sawer_sentences[-1]
    word_count = len(last_sentence.split())
    print("Task 10:", word_count)
else:
    print("Task 10: Нет предложений")