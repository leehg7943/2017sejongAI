

가설1 : 직접적으로 별을 매기면 수치에 영향이 있을 것이다.

  보통 리뷰를 한 줄로 함축할 때, 별점으로 리뷰를 매기 때문에 별점이
  중요할거라 생각했다.

  긍정적(99%)인 리뷰

  "Home Alone is a hilarious film about a young boy (Macaulay
  Culkin) who is accidently left home during the Christmas holidays after the
  rest of his family goes to Europe." "At first Culkin loves the
  situation, but soon he is scared to death when he learns that burglars Joe
  Pesci and Daniel Stern are targeting his house." "However, Culkin is
  pretty smart for an eight-year-old and he has plans for them when they
  attack." "Chris Columbus' direction is smart and so is the
  over-achieving screenplay." "This film has a little bit of something
  for everyone and the fact that the backdrop is the Christmas holidays, only
  makes it that much more special." "All the performers do well and in
  the end the film also does." "4 stars out of 5."

  ->여기서 마지막 문장을 빼거나 숫자를 다르게 하거나 ‘This is 0
  star’를 추가해도 probability가 0.99로
  동일했다.



  부정적(59%)인 리뷰

  Some of Sacha Baron Cohen's movies contain a modest amount of
  comedy. Most of them are just stupid, gross humor. If you have an IQ under 60
  you may find them amusing. I understand that comedy is not the same for
  everyone but after a few minutes of this movie I was heading for the exit. I
  did not see or hear anyone in the theater laughing. The comedic skits in this
  movie fall so flat you can hear the thud. Not sure who green-lighted this movie
  but whoever it was should be taken out and flogged. Unless you can find this in
  the $1 bin at your local discount store (and it is headed there, take my word)
  I would avoid it like the plague. What a flop. What were Mark and Penelope
  thinking when they signed on for this stinker?

  ->처음에는 negative가 0.59였는데
  마지막에 ‘This is 0 star’를 추가했을 때는 0.71, ‘This
  is 1 star’를 추가했을 때는 0.65, ‘This is 5star’는 0.59로 나왔다. 그래서 별을 언급했을 때, 차이가 있을거라 생각했으나 ‘4 stars out of 5.’를
  추가했을 때는 0.71이었다.

 

가설2 : 문장에 대한 수식이 많을수록 정확도가 높아진다.

  형용사구에는 직접적, 간접적 묘사가 많기 때문에 영향을 끼칠 것이다.

  긍정적(99%)인 리뷰

  "Home Alone is a hilarious film about a young boy (Macaulay
  Culkin) who is accidently left home during the Christmas holidays after the
  rest of his family goes to Europe." "At first Culkin loves the
  situation, but soon he is scared to death when he learns that burglars Joe
  Pesci and Daniel Stern are targeting his house." "However, Culkin has
  plans for them when they attack." "Chris Columbus' direction is smart
  and so is the over-achieving screenplay." "This film has a little bit
  of something for everyone and the fact that the backdrop is the Christmas
  holidays" "All the performers do well and in the end the film also
  does." "4 stars out of 5."

  ->여전히 99%임.



  부정적(59%)인 리뷰

  Some of Sacha Baron Cohen's movies contain a modest amount of
  comedy. Most of them are just stupid, gross humor. If you have an IQ under 60
  you may find them amusing. I understand that comedy is not the same for
  everyone. The comedic skits in this movie fall so flat you can hear the thud. Unless
  you can find this in the $1 bin at your local discount store (and it is headed
  there, take my word) I would avoid it like the plague. What a flop. What were
  Mark and Penelope thinking when they signed on for this stinker?

  ->66%로 변화했음. 묘사를 하면서 비판을 하는 문장을 제외시켰더니
  예측과 다르게 정확도가 더 상승했음.

 

가설3 : 핵심적인 단어가 쓰인 문장을 빼면 수치가 달라질 것이다.

  긍정적(99%)인 리뷰

  "Home Alone is a hilarious film about a young boy (Macaulay
  Culkin) who is accidently left home during the Christmas holidays after the
  rest of his family goes to Europe.” "However, Culkin is pretty smart for
  an eight-year-old and he has plans for them when they attack." "Chris
  Columbus' direction is smart and so is the over-achieving screenplay." "This
  film has a little bit of something for everyone and the fact that the backdrop
  is the Christmas holidays, only makes it that much more special." "All
  the performers do well and in the end the film also does." "4 stars
  out of 5."

  에서 love가 사용된 문장을 제외시킨 결과 86%로 달라졌다.

  "At first Culkin loves the situation, but soon he is scared to
  death when he learns that burglars Joe Pesci and Daniel Stern are targeting his
  house."



  부정적(59%)인 리뷰

  Some of Sacha Baron Cohen's movies contain a modest amount of
  comedy. I understand that comedy is not the same for everyone. The comedic
  skits in this movie fall so flat you can hear the thud. Unless you can find
  this in the $1 bin at your local discount store (and it is headed there, take
  my word) I would avoid it like the plague. What a flop. What were Mark and
  Penelope thinking when they signed on for this stinker?

  Stupid가 사용된 문장을 제외시키니 54%로 달라졌지만 큰 차이는
  없었다.

  Most of them are just stupid, gross humor. If you have an IQ under
  60 you may find them amusing.

