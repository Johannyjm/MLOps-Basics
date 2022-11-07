import hydra
from omegaconf import OmegaConf

@hydra.main(config_name="config")
def main(cfg):
    # Print the config file using `to_yaml` method which prints in a pretty manner
    print(OmegaConf.to_yaml(cfg))

if __name__ == "__main__":
    main()

