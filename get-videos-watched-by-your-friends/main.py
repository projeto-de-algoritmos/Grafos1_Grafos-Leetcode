#!/usr/bin/env python3
from collections import Counter


class Solution:
    def watchedVideosByFriends(
        self,
        watchedVideos: list[list[str]],
        friends: list[list[int]],
        id: int,
        level: int,
    ) -> list[str]:
        # g is the connection graph
        g = set([id])

        # store the visited nodes
        visited = set([id])

        # we are only interested in elements exactly `level` nodes away.
        for _ in range(level):
            # get nodes at this level
            # we need to override the graph to only store the nodes in this
            # level and that were not visited yet
            g = {k for i in g for k in friends[i] if k not in visited}

            # update visited set to include nodes we visited in this level
            visited |= g

        # after finishing the loop, `g` should contain only the friends with
        # distance `level`

        # count the frequency of the videos watched by friends
        frequencies = Counter(video for i in g for video in watchedVideos[i])

        # sort the videos
        # the key is (frequency, video_name), since the frequency has priority
        return sorted(frequencies.keys(), key=lambda x: (frequencies[x], x))


assert Solution().watchedVideosByFriends(
    [["A", "B"], ["C"], ["B", "C"], ["D"]], [[1, 2], [0, 3], [0, 3], [1, 2]], 0, 1
) == ["B", "C"]

assert Solution().watchedVideosByFriends(
    [["A", "B"], ["C"], ["B", "C"], ["D"]],
    [[1, 2], [0, 3], [0, 3], [1, 2]],
    0,
    2,
) == ["D"]
