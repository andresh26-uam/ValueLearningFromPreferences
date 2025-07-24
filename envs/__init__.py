from gymnasium.envs.registration import register

register(
     id="RouteChoiceEnvironmentApollo-v0",
     entry_point="envs.routechoiceApollo:RouteChoiceEnvironmentApollo",
     max_episode_steps=1,
)

register(
     id="RouteChoiceEnvironmentApolloComfort-v0",
     entry_point="envs.routechoiceApollo:RouteChoiceEnvironmentApolloComfort",
     max_episode_steps=1,
)