---
layout: wiki
title: Game Rules
permalink: /teko/wiki/rules/
# --- FILA 1: NAVEGACIÓN ---
header_buttons_row_1:
  - label: Home
    url: /teko/

  - label: Announcements
    url: /teko/announcements/

  - label: Presskit
    url: /teko/presskit/

  - label: Wiki
    url: /teko/wiki/

# --- FILA 2: SOCIAL Y DONATE ---
header_buttons_row_2:
  - url: https://store.steampowered.com/developer/TalioGames
    icon_class: fab fa-steam
    new_tab: true
    custom_class: "steam-desktop-margin"

  - url: https://discord.com/invite/Xk8RxfWBn6
    icon_class: fab fa-discord
    new_tab: true

  - url: https://www.youtube.com/@TalioGames
    icon_class: fab fa-youtube
    new_tab: true

  - url: https://x.com/TalioGames
    icon_class: fab fa-twitter
    new_tab: true

  - label: Donate
    url: https://patreon.com/c/TalioGames
    new_tab: true
---

<h2 style="text-align: center;">Rules & Glossary</h2>

**STATS**
* **Mana**: 3 by default. Mana determines how many plays you can make. Every time you play a hand, you'll lose 1 mana. When it reaches 0, if you still haven't reached the score goal, you'll lose. It refreshes every round.
* **Discards**: 4 by default. This is the number of discards you can make. When selecting chips you can discard them to draw the same amount from the deck. Each discard consumes 1 available chance. It refreshes every round.
* **Shuffle**: 2 by default. Whenever the deck runs out of chips, the discarded chips will be shuffled and returned to the deck so you can keep drawing. Once you run out of available shuffles, you won't be able to do it again and you'll have to win the round with the remaining chips on the table.
* **Play size**: 5 by default. This determines the size of your hand. You can select chips up to the play size limit.
* **Draw size**: 8 by default. This determines the size of your table. Whenever you draw chips because you've played a hand or discarded, the table will refill up to the draw size limit. The maximum default draw size is 13.

**PLAY MECHANICS**
* **Turn**: 3 by default. The number of available turns depends on the remaining mana.
* **Round**: 19 by default. Every time you enter the scoring screen, a new round begins.
* **Stage**: 6 by default. The first stage has 4 rounds; the others have 3. Each stage features a random boss.
* **Score goal**: The number of points that must be reached each round. Each run requires a specific amount of points (except in the first round), which depends on how much the player's build has grown. Reaching the score goal moves you to the shop and the next round.
* **Overkill**: The excess score compared to the score goal, measured as a percentage (if the score goal is 100 and you score 200, that's 100% overkill). This will increase the next score goal, but you'll earn $1 for every 10% overkill (up to $30, meaning 300%) at the end of each round.
* **Interest**: Every time you finish a round, before entering the shop, you'll earn money depending on how much you've saved. By default, you'll earn $1 for every $3 saved, up to +$9 ($27 saved).
* **Passive earnings**: The player earns money for winning each round. 1–4 = $1; 5–12 = $2; 13–18 = $3; 19–21 = $4.
* **Color tubes**: Each tube corresponds to one of the four colors. Playing a chip increases the counter of its corresponding color tube. When it reaches the maximum (12 by default), activating the tube triggers a special effect. There's also a multicolor tube, which fills by activating the other four tubes. When it reaches its maximum (7 by default), you'll gain a special multicolor pack. The other tubes do the following: Orange: +1 draw this turn and the next turn; Green: reduces the score goal by 15%; Pink: x1.5 multi this turn (applies at the end of the entire chain but before special combo); Cyan: +1 play size this turn.
* **Cookie tray**: Depending on the chip's shape, a slot will be filled. Each container depends on the number of corners the shape has. Score 6 hexagons, 5 pentagons, 4 squares and 3 triangles in total to fill the tray. Doing so grants a special shape pack. You can reduce the number of shapes required to a minimum of 7.
* **Pillbox**: Fill the pillbox with 10 pills (one of each number). Each chip played with a different number fills the empty slots of the pillbox. Once completed it resets and you'll gain a random consumable. You can reduce the number of pills to place to a minimum of 4.
* **Pirinola**: Before starting a round you'll have to spin the Pirinola, which has 5 faces. The lower faces have higher chances to appear and will increase the score goal percentage but grant money in return. The higher the face, the more money it grants and the more the score goal increases.
* **Bosses**: Every 4 rounds you'll fight a boss. Each boss applies a debuff only during its respective round. After defeating 2 normal bosses (red frame) you'll fight a special one (gold frame), which usually has stronger effects that impact gameplay more. Under certain conditions (high pocket deepness) it's possible to fight 2 bosses at once. In that case it alternates between 2 normal bosses or 1 normal boss + 1 special boss (two mana-removing bosses will never appear together).
* **Perks**: Every time you defeat a boss, you'll earn a perk. Each perk can only be obtained once (except for efficiency ones, these can be obtained twice), and you have a 10% chance to get a special one (which are much better than normal ones, for example, extra mana).

**SCORING**
* **Base/Multi**: The two key values that determine the score earned each round. The formula is a multiplication: Base * Multi. Base is usually much easier to obtain (mainly by scoring chips). Multi is rarer but it's very easy to obtain items (especially cards) that multiply it.
* **Combos**: You can perform up to 3 combos at once. The rarer the combo, the more Base and Multi it grants. Colors/shapes can't score 'Straight', and numbers can't score '4 different'.
* **Levels**: When leveling up combos, the following formula applies: New Base Value = ceil(previous_base * 1.09) + 5; New Multi Value = ceil(previous_multi * 1.08) + 3. '4 different' and 'straight 3' share the same level, just like 'double pair' and 'straight 4'. When one levels up, the other levels up as well.
* **Extra points**: Each combo grants a fixed amount of extra points. These extra points determine how much extra base x multi you'll generate (see the table at the bottom of the manual). Every 7 combo levels gained, extra bonus base is multiplied by 1.2 and multi by 1.1, rounded up.
* **Special combos**: A pink text will appear in the middle of the screen indicating the combo will trigger. Each time it's played, the combo loses 0.5 value (but it still has a minimum value). To obtain it you must combine 3 combos at once: Trixi (x3 - x1.25) Straight 3 of number + Trio of color and shape / Trihostel (x3 - x1.25) Full mansion with the 3 traits / Tekano (x4 - x1.5) Straight 4 or Quadra with number + Quadra of color and shape / Teko (x5 - x2) Straight 5 or Penta with number + Penta of color and shape.
* **Selection**: Selecting chips reveals the base x multi amount of each trait and the resulting combo, as well as the extra bonus points counter (depending on how full the tube is it will move to the next level). Selection order doesn't break combos (there are no chip chains, for example selecting a Straight out of order will still execute it), and the highest category combo will always trigger (in the manual, combos lower on the list have higher priority).
* **Scoring order**: Chips > (Combos) Number / Shape / Color > Mods > Cards > Pink tube > Special combo.

**ITEMS**
* **Pockets**: In the main menu you can choose the desired pocket. Each one has a distinct mechanic and the balance differs between them. All present a different challenge and a noticeable playstyle. Each has 5 difficulties (deepness) from 0 to 4. To unlock new pockets you must win runs with other pockets on difficulties 0/2/4.
* **Chips**: Depending on the number and shape, each chip has a defined base value. For example a 'triangle 7' adds 10 base points (3+7). By default you can have at least 20 chips inside the pocket. They're the first factor influencing scoring because they score before combos, mods and cards. They score from left to right.
* **Stickers**: These are located inside chips. Stickers can have different fill shapes and colors. Shapes and colors are two different traits and can be combined in any way. Stickers usually activate when the chip they're equipped on activates.
* **Cards**: There are 5 rarities (Common, Rare, Epic, Supreme, Forbidden). They usually execute from left to right, but each card can act at different moments of the run, for example when chips trigger, when entering the shop, when using an item, etc. Cards have 4 traits: Action, cards that execute in order after mods; Unsellable (can't be liquified either); Indestructible (prevents being destroyed by killer cards); Unique (you can only have one). By default, you have 12 slots for your cards, with 6 unlocked from the start. The rest can be unlocked in the store for $4, $7, $10, $13, $16, and $20, respectively.
* **Mods**: Equipped on cards and used to gain advantages. Each card rarity has a default number of mod slots (4/3/2/2/0). There are 3 mod rarities: Common (1 slot), Rare (1 slot), Pro (3 slots). They can be unequipped and transferred between cards only on the shop screen. They trigger from left to right.
* **Consumables**: There are 3 slots to store consumables. Some can only be used in the shop and others only during rounds (this is indicated in the tooltip). There are 3 rarities: Common, Rare, Epic.
* **Packs**: Opening them grants the item indicated in their description.

**MISC**
* **Selling**: You can sell all the items you've purchased, usually for half their value according to the shop, except for consumables, which won't give you any money back if you bought them; however, if you obtained them through other ways, they will still have some value.
* **Reroll**: Up to 5 rerolls can be made, costing $2/4/6/8/10. Doing so refreshes all items in the shop, presumably ensuring different ones appear. By default cards already purchased and still in your inventory won't appear again. The more rerolls performed, the higher the chances of getting high rarity cards and consumables.
* **Lock**: Up to 2 items can be locked in the shop. This prevents them from disappearing when rerolling or leaving the shop. You'll lose $1 for each locked item every time you enter the shop or reroll.
* **Pity**: Depending on the selected pocket and its deepness, you'll get 2 different traits: guaranteed cards when entering the shop on a certain round, and a restriction on obtaining high rarity cards and consumables unless you perform at least 2 rerolls or reach a certain round.
* **Forbidden appearance rate**: By default it's 1%, but it decreases as deepness increases. This rate is fixed for all forbidden cards. Each interacts with a different mechanic. For example, Teko Card has between 1% and 0.1% chance to appear whenever a penta combo is executed. If this chance occurs and you don't have enough space in the card inventory, the leftmost card will be removed automatically to make room.
* **Codex**: Currently located in the main menu and in the options screen in the bottom-left corner. Entering the codex lets you see all available items, including those locked by achievements (hovering over them will show the requirements to unlock them).