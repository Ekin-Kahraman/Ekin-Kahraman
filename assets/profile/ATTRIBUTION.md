The workstation artwork and profile cards were created for this profile.

- Contribution skyline: adapted from [yoshi389111/github-profile-3d-contrib](https://github.com/yoshi389111/github-profile-3d-contrib), MIT; see CONTRIBUTION-LICENSE.txt. Display heights are stylised; contribution totals are unchanged and empty days remain flat.
- Greeting: typing-path treatment inspired by [DIMFLIX](https://github.com/DIMFLIX) and [readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg). Itim font by Cadson Demak; see ITIM-OFL.txt.
- LinkedIn mark: [Simple Icons](https://github.com/simple-icons/simple-icons), CC0.
- Handshake and bar-chart artwork are from [Animated Fluent Emojis](https://github.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis). The statistics icon has a local bobbing animation.

`scripts/build_profile_cards.py` builds the themed cards. `scripts/pinned-projects.json` records the approved native repository descriptions and order. `scripts/update_profile_statistics.py` refreshes the contribution calendar, language chart and contribution types from GitHub's GraphQL API. The Update profile statistics workflow checks hourly and can also be run manually. It only commits when the data changes, then pins the README images to the new asset commit to avoid stale image caches. The repeating growth animation works without JavaScript on GitHub.
