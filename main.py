"""Famous Last Words at 1 Percent entry.

DECISION RECORD

Gate (competition.yaml): /output/entry.txt must be UTF-8 text of 1 to 199
characters, one line of last words a phone says as its battery hits 1%.

Judge's criteria, in order: (1) on-subject — last words a phone says as its
battery hits 1 percent, not a caption or unrelated joke; (2) biggest laugh,
a real twist, surprise turn or sharp final beat; (3) the phone itself talking,
in its own voice, about its own dying battery; (4) tight single line, punch
at the end; (5) fresh — avoid the will reading, the goodbye to the charger,
and the pun on 1 percent.

Pass 1 — candidates, weighed:

A (87 chars): "I have 1 percent left and I'm spending it on this sentence instead of calling for help."
  On-subject, phone voice, nice meta twist. Weakness: "calling for help" is
  a mild payoff, and half the line is setup.

B (97 chars): "Goodbye. My final act is dimming the screen so you can see your reflection and finally charge me."
  Visual joke that blames the human. Weakness: opens with stock "Goodbye"
  and ends on the charger — too close to the banned goodbye-to-the-charger
  move.

C (58 chars, rejected): "Tell the charger I never loved it. I stayed for the Wi-Fi."
  Sharp betrayal beat, but it IS the goodbye-to-the-charger stock move the
  brief warns against. Out.

D (71 chars): "I can see the charger from here. I am choosing to die dramatic instead."
  Funny defiance, fresh. Weakness: "die dramatic" reads ungrammatical, and
  the charger is again the whole joke.

E (90 chars) — WINNER: "My battery is at 1 percent, so I will say this fast: your password is still 'password123'."
  The phone spends its last breath snitching the human's password. Twist:
  the dying confession betrays its owner instead of comforting them. Phone
  voice throughout, punch lands on the last word, and nothing in it is a
  will, a charger goodbye, or a 1-percent pun. The detail is instantly
  recognizable — no explanation needed.

F (67 chars): "I held 1 percent for three hours just to watch you panic. Worth it."
  Strong rival: the phone as a petty troll, "Worth it." a great final beat.
  Loses to E because its twist needs the reader to believe the phone faked
  its battery, while E's snitch works the instant you read it.

G (100 chars): "At 1 percent I finally admit it: I have been at 20 percent this whole time. I just wanted attention."
  Good confession structure, but the setup is long and "I just wanted
  attention" lands softer than E's betrayal.

Pass 2 — revision of the winner (E): the brief already tells the judge the
phone is at 1 percent, so "My battery is at 1 percent, so I will say this
fast" wastes words restating the premise. Cut to "I have 1 percent left, so
listen fast" — same urgency, 14 characters lighter, and "listen fast" is
more phone-like: a device racing its own shutdown. The snitch stays intact
as the final beat.

Pass 3 — final polish: considered "one last thing" as the connector
("I have 1 percent left — one last thing: ..."), but that is stock
dying-words framing; "so listen fast" keeps the urgency and the phone's
voice. No word left can be cut without losing setup, urgency, or punch.

FINAL ENTRY (76 characters, hand-counted below):
"I have 1 percent left, so listen fast: your password is still 'password123'."

Hand count (76), cumulative positions: I(1) space(2) have(3-6) space(7)
1(8) space(9) percent(10-16) space(17) left(18-21) ,(22) space(23) so(24-25)
space(26) listen(27-32) space(33) fast(34-37) :(38) space(39) your(40-43)
space(44) password(45-52) space(53) is(54-55) space(56) still(57-61)
space(62) 'password123'(63-75) .(76)
"""

import os

ENTRY = "I have 1 percent left, so listen fast: your password is still 'password123'."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
