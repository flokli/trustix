package config

import (
	"github.com/BurntSushi/toml"
)

type GitStorageConfig struct {
	Remote   string `toml:"remote"`
	Path     string `toml:"path"`
	Commiter string `toml:"commiter"`
	Email    string `toml:"email"`
}

type NativeStorageConfig struct {
	Path string `toml:"path"`
}

type StorageConfig struct {
	Type   string               `toml:"type"`
	Git    *GitStorageConfig    `toml:"git"`
	Native *NativeStorageConfig `toml:"native"`
}

type ED25519SignerConfig struct {
	PrivateKeyPath string `toml:"private-key-path"`
}

type SignerConfig struct {
	Type      string               `toml:"type"`
	KeyType   string               `toml:"key-type"`
	PublicKey string               `toml:"public-key"`
	ED25519   *ED25519SignerConfig `toml:"ed25519"`
}

type LogConfig struct {
	Name    string         `toml:"name"`
	Mode    string         `toml:"mode"`
	Storage *StorageConfig `toml:"storage"`
	Signer  *SignerConfig  `toml:"signer"`
}

type Config struct {
	Logs []*LogConfig `toml:"log"`
}

func NewConfigFromFile(path string) (*Config, error) {
	conf := &Config{}

	if _, err := toml.DecodeFile(path, &conf); err != nil {
		return nil, err
	}

	return conf, nil
}