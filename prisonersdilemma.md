# organized notes

## Articles and papers

Most interesting results: 8 and 10.

Good introductions: 1,2,3,4,9, in that order.

1. [Wikipedia on Prisoner's Dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma). DONE; very useful.
2. [Overview of the Axelrod Tournaments](https://egtheory.wordpress.com/2015/03/02/ipd/). DONE; relatively helpful.
3. [Effective Choice in the Prisoner's Dilemma](https://www.jstor.org/stable/pdf/173932.pdf?refreqid=excelsior%3Af5b158611a3af6d40ee4c21e928ee42a) (Axelrod's First Paper). DONE; good introduction. Background on why TFT is seen as dominant.
4. [More Effective Choice in the Prisoner's Dilemma](https://artisinternational.org/articles/Axelrod_Prisoners_Dilemma.pdf). (Axelrod's Second Paper. DONE; essential follow-up to the previous paper. TFT wins again.
5. [The Evolution of Cooperation](http://www.sfs.uni-tuebingen.de/~roland/Literature/Axelrod(81)_the_evolution_of_cooperation.pdf). A book by Axelrod as a follow-up to his previous two papers. NOT READ; does not seem super relevant.
6. [Zero-Determinant Strategies](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3387070/pdf/pnas.201206569.pdf). SKIMMED. Recent, seems interesting. Also seems like it's not as cool as it sounds; there are a lot of assumptions in it (e.g. only memory of the latest move, and only played against players that are "evolutionary" which means that they can't have an adaptive strategy).
7. [Comment on Zero-Determinant Strategies](https://golem.ph.utexas.edu/category/2012/07/zerodeterminant_strategies_in.html). DONE; states that the zero-determinant strategies do not beat tit-for-tat, but that they are interesting on their own in the sense that they can not only win but also control the game. The important thing to note here is that this is not considering a multiplayer approach.
8. [Evolution and Cooperation in Noisy Repeated Games](http://www.dklevine.com/archive/refs4546.pdf). This seems to be exactly what I was thinking: looking at the equilibrium state and showing that tit-for-tat etc are evolutionary stable while other strategies are not. It does introduce the interesting idea of noise, however, which I might be able to use.
9. [Emergence of cooperation and evolutionary stability in finite populations](https://www.nature.com/articles/nature02414.pdf). This also seems very much in line with what we were thinking. This paper is not trying to find the optimal strategy, or a "winner" of sorts, as the other papers have tried to, but rather tried to explain under the least set of assumptions how a cooperative strategy like TFT could win against a non-cooperative strategy like AllD in finite populations. This is arguably of high interest as it can readily be applied to actual real-life situations to explain why cooperation can arise. This paper is also really really good (easy to follow, well structured, etc etc) and has references to lots of previous literature. However: it only proves that AllD is not evolutionary stable, and does not say anything about strategies that are very similar to AllD in that they do not generally cooperate, which makes it less interesting.
10. [Evolutionary Stability in Repeated Games Played by Finite Automata](https://deepblue.lib.umich.edu/bitstream/handle/2027.42/29923/0000280.pdf%3Bjsessionid%3DAEAFA5FC409CD192FED110736FBDE473?sequence%3D1). This is interesting. It proposes a modified notion of evolutionary stability (called MESS) that states that a strategy with fewer states in its finite automaton can invade a strategy with more states even if they receive the same payoffs. Then, they are able to prove that there exists a 2-state MESS (tat-for-tit), and also that for a strategy to be a MESS it needs to be utilitarian (i.e. get highest payoff with itself). The idea is kind of that a strategy that is not utilitarian can be invaded by a simplified version of itself that only contains the states it has when playing against itself, and then that version can be invaded by someone taking advantage of it. This is actually very reasonable. It is, however, somewhat arbitrary to always prefer strategies with fewer states, which is the critical assumption leading to these results. They also include a discussion in the end of what happens when there are multiple strategies that all cooperate with each other. It would be nice to be able to relax the assumption of preferring fewer states.
11. [Evolutionary Games and Spatial Chaos](https://www.nature.com/articles/359826a0.pdf). Not super relevant but actually really cool: patterns can arise if we play the game on a grid. Not sure how actually profound this is.

## The State of Current Knowledge

1. In the non-repeated deterministic game, AllD is optimal.
2. In the finitely repeated deterministic game, AllD is not evolutionary stable.
3. In the infinitely repeated game with (weird) noise, a strategy can only be evolutionary stable if it is utilitarian.
4. In the infinitely repeated deterministic game where the number of states in the finite automaton affects its fitness, a strategy can only be evolutionary stable if it is utilitarian.

(The reason that 3 is weird is that it says that TFT is utilitarian with noise, when it isn't if you model noise as having a probability $p$ of making a mistake at every step (no matter how small $p$ is). So the model just doesn't model real noise very well.)

### Conjecture: To be evolutionary stable in a (good) noisy model, a strategy needs to be utilitarian

This conjecture would be a stronger result than what is currently known. (In particular, it uses a definition of evolutionary stable that is weaker than what is used in 4, so the result would thus be stronger than the one there while also having less assumptions.)

recent update: I do not anymore think that this works. see ipad notes.

Note: Most of the below has been transferred to the LaTeX document.

A lot to unpack here.

- Evolutionary stable: if an infinitesimally small population of another strategy is injected, that strategy does not take over.
    - Could potentially modify this to: if a fraction $f$ of the population is of another strategy...
    - This modification would lead to 1: the choice of a parameter and 2: a stronger definition of ES
- Noisy model: here we have a choice. Fudenberg and Maskin went with the infinitesimally small route, which seems weird. Going with a constant probability $p$ of a mistake seems more valid in real life. Even then, there are a few choices of how to define this, as outlined below.
- Strategy: a finite automaton whose input is the opponent's move on the previous turn, and where every state has a designated output.
    - Potential modification: let the output be probabilistic. Could also let the transitions be probabilistic, which might (??) be equivalent.
- Efficient with itself: when played against itself, the strategy obtains the maximum payoff.
- General setup: infinite games, looking at the time-average payoff.
    - Potential modification: finite games (possible edge effects, weird things)
    - Potential modification: discounted payoff (would be more sensitive to weird behaviors, possibly better)

Plan for proving the conjecture:

- Start with a model that is the most similar to Fudenberg and Maskin's model.
- Change one thing: add error probability $p$ instead of infinitesimally small errors which are weird
    - Have to look at expected payoff, then
- Prove it
- Then relax or justify the other assumptions too

There are two ways to model the noise:

1. There's a probability $p$ of interpreting the opposite move by the opponent. Or, in other words, there's a probability $p$ of transitioning to the wrong state in the finite automaton.
2. There's a probability $p$ of taking the wrong action (but you always follow the correct transition).

I feel like these are largely equivalent: there's a difference in the actual interaction when the mistake occurs, but not in any future moves. So it is very likely that they will both produce the same conclusion, which means that I should go with the one that is easiest.

## Meeting 2/13

Evaluating?

- Average against every possible sequence of moves. Seems bad.
- Evolutionary tournament.
- Two-player tournament but also play against yourself.

Thoughts:

- There are two different ways of looking at it: 1v1 or multiplayer.
- For multiplayer there's the classical Axelrod tournaments, where humans submitted strategies and Tit-for-tat won twice.
- Axelrod also simulated the strategies and showed that Tit-for-tat would continue winning, if we assume an ecological model.
- There seems to not have been much more work on this multiplayer model of IPD.
- For 1v1 there's a relatively recent paper that shows that a player can force the ratio (a-1)/(b-1)
to be what they want (I think). Basically they're showing that remembering more than 1 round back is not beneficial and then they can model the outcomes as a Markov chain and then do some linear algebra to get to a stationary distribution.
- In my opinion the 1v1 game is not very interesting, because if the only criteria is winning then you can easily construct a strategy that just does that.
- So I want to focus on the multiplayer mode, because I think that that is what most accurately reflects how we want to use the prisoner's dilemma, and where it will make sense to cooperate.
- The question is what context we want to use. The problem with Axelrod is that it doesn't really show anything. Ideally we'd want some sort of evolutionary tournaments, because that is what most accurately reflects what we want. The question would be if there is some sort of equilibrium state and if the equilibrium is exactly tit-for-tat, or if all tournaments will just start cycling in some sort of rock-paper-scissors manner (or I suppose you can ensure that you don't get a cycle like that by including probabilistic strategies). Are there multiple equilibrium states?
- That is the idealized picture, but it seems very hard. You could also run one strategy against all other possible strategies but then always-defect is the best strategy and it does not really reflect what we're actually trying to calculate. I also considered only having two players but they also play against themselves, and I think you can easily prove that tit-for-tat is optimal in this case (in the sense that there is no strategy that wins against tit-for-tat). So that is already interesting. The reason why that is a valid way to look at it is that playing against yourself is sort of like cooperating with someone which is what would happen in the real world. (tit-for-tat: if opponent ends with cooperate, then they're equal, and if opponent ends with defect, then the opponent wins by 5 points). Hmm this might not be as trivial as I thought. (I can say that I just thought about this situation.)
- Plan for next week: read the zero-determinant paper, read the numerical paper on number of rounds vs number of memory, make sure that I've exhausted all available information online, and formulate a question that can reasonably be answered.

OK so let's do the 1v1 + play yourself using finite automata. I think it will be possible to prove something with it.

#### Additional thoughts

1. 1v1 but also play against yourself. Failed because degenerate strategy exists: "Start with 'd'. If opponent also does 'd', then always do 'c'. If opponent does 'c', then always do 'd'." This degenerate strategy is a very simple finite automaton.
2. Average against all possible players. Then always 'd' wins. The reason is that a bunch of stupid strategies exist that are good for the always 'd' player.

Maybe 1 is not degenerate? We can extend it to always go to always 'd' as soon as it finds out it is not playing against itself. So in a sense it is colluding with itself, and not really being a helpful good strategy at all that would fare well in the real world.

Hmmm I'm wondering if it helps to do 2 but with two opponents? Do we still have the problem with the stupid strategies? Yes I think we do. Actually, what is the difference between the stupid strategies and the not-so-stupid strategies?

OK, so there are two more restrictions that I might place. One is that you can only take decisions based on the N most recent moves, which can be simplified further to only the single most recent move.

So one stupid thing that will work is to extend the 1v1+self idea to be infinite. Then TFT would be optimal. But so would many many other strategies, so this is not really useful at all. Damn. Why is this so hard.


## Meeting 2/19

#### Pre-meeting

I've tried my two main ideas, but neither of them worked.

Overarching problem: just play against 1 opponent then always defect wins.

Idea 1: you play a round-robin tournament of all possible strategies within some small set of strategies. I first tried only the four simplest strategies. Then always defect wins. Then I realized that in any family of strategies like that, always defect will always win (the proof for this is simple: consider 1 given strategy, and construct a tree based on what the opponent does. the claim is that all branches of the tree are equally likely, and the proof is that for any given sequence of historical information and machine configuration there exists 1 strategy that outputs defect and one that outputs cooperate, so all branches are equally likely. therefore it all reduces down to only a 1-round game which always defect wins.). So to get interesting results you would somehow need to select a subset of strategies that only contains smart strategies, and the only way I can see how to do that would be through an evolutionary model.

Idea 1: you play against your opponent and also against yourself. Here TFT wins against AllD, which is really good. And if you consider the infinite length game and deterministic strategies, then in a sense TFT is unbeatable. This carries over to randomized strategies if 3 + 3 > 5 (which it should be), because tft loses with at most 5. But in finite games this can be improved with a self-identifying strategy, which kind of suggests that this approach is not very good.

Problem: a self-identifying strategy like below.
1. Defect on round 1.
2. If opponent defects on round 1, always cooperate. Else, always defect.

This strategy is in a rock-paper-scissors relationship with TFT and AllD (in the model of playing your opponent and yourself), which is not good.

#### Post-meeting

Two new ideas: 

1. introduce noise, and 
2. look at the weighted version of playing against yourself and playing against your opponent. 

Idea 2 came first, and it came from the realization that both models that I had investigated did not really represent reality very well. The round-robin of all strategies includes too many suboptimal strategies that makes it not represent reality because reality has an evolutionary aspect to it. But an evolutionary process is hard to analyze. One possible thing to do would be to analyze the stable state, because we might not be able to say that every state will end up with tit for tat but if we can at least show that tit for tat is indeed stable then it is interesting.

So you want to analyze stable states. One way to do it is to introduce a small group of strategies in a bigger group of strategies. This we realized is the same as a weighted version of the play-against-yourself strategy. I brought up the problem of the self-identifying strategy, and how it forms a rock-paper-scissors relationship with self-identifying > tft > dd > self-identifying, but then we realized that if we in the weighted version give less than 0.5 weight to the self-identifying in the self-identifying vs tft scenario, then tft will prevail and we won't really have a problem. 

Another interesting thing to consider is the introduction of noise. There are several ways to add noise; what we considered was adding a failure probability in how you perceive your opponent's last move. This causes tit-for-tat to potentially end up in an alternating pattern from just a single failed signal, which suggests that maybe tit-for-tat is not the best strategy in this context. Adding noise is also defensible in the sense that it is quite likely that real situations also have noise in them, and you could also always set the noise to 0 to get to the original situation.

So the idea, then, is to analyze the following situation:

- You have two strategies A and B.
- You have an error probability of p.
- You consider a population where there is x% of B and (100-x)% of A.
- You find the biggest x such that A still wins.
- Potentially, you can start with the question: does there exist a fixed x such that A still always wins? For which strategies?
- Note again that this more or less means that you're just playing A against B, A against A and B against B, and then you weight the matches differently.
- Note that this model makes sense from a reality perspective, which is good.

Steps to take:
- Deep-read `Evolution and Cooperation in Noisy Repeated Games`. I think that this is very similar to what we just thought of.
- Look at all articles that cite that article.
- Figure out if there is still something to do here.
- If so, do it.

## Meeting 3/4

#### Pre-meeting

So it seems like this problem is more well-studied than I first thought. (see the `Emergence of cooperation and evolutionary stability in finite populations` paper and its references)

Maybe it is possible to combine the finite populations idea with the possibility of mistakes? It seems like we might get a two-dimensional problem here then which might be very hard but it might also be interesting to study.

Oh ok so that theorem (from `Evolution and Cooperation in Noisy Repeated Games`) is not strong enough to prove that a strategy that is nice against itself must be nice against an opponent. But maybe it is also possible to prove that an evolutionary stable strategy not only is efficient with itself but also efficient with any other strategy that is efficient with itself.

(Because the current state of affairs does not exclude a situation where one strategy is dominant but still not very nice. Like if it only collaborates with itself, is it truly a cooperative strategy? I'd say no.)

So the current state of affairs is that it has been showed that:

1. for infinite games with infinite populations and an error probability, a strategy must be efficient with itself to be evolutionary stable, and 
2. for finite games with finite populations, AllD can sometimes be more likely than not to be replaced. 

I think that (1) is interesting (BUT the noise is modeled in a weird way), but it doesn't say anything about what a strategy can do with another strategy — i.e. it doesn't say that the strategy has to be nice to another strategy. 

I think the following should be possible to prove (from the model presented in `Evolution and Cooperation in Noisy Repeated Games`):

- To be evolutionary stable, a strategy also needs to be nice to all other nice strategies.

Possible ways of doing this:

1. actual error probability,
2. use their framework and show that a strategy also needs to be nice to other nice strategies

#### Post-meeting

The idea of the family of strategies that are all nice to each other, that I think might be possible to prove, would not agree well with reality — in real life there are different clans that cooperate internally but not with each other.

Maybe the way that the `Evolution and Cooperation in Noisy Repeated Games` paper handles noise is suboptimal? That is, it doesn't say much about what would happen in real life, because in real life noise doesn't follow this model. This could explain why the paper's assumptions could have implications as the one above that is not reflected in the real world.

1. Consider what happens in `Evolution and Cooperation in Noisy Repeated Games` if the noise is modeled as a fixed probability $p$ of ending up in the wrong state in the finite automaton.

Most work from now on is in the latex document.