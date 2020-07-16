#pragma once
#include <random>
#include <vector>

class Random 
{
private:
	std::mt19937 mt;
public:

	inline Random(int seed) {
		mt = std::mt19937(seed);
	}


	inline double random() {
		std::uniform_real_distribution<double> dist(0.0, 1.0);
		return dist(mt);
	}

	inline int randInt(int max) {
		std::uniform_int_distribution<int> dist(0, max - 1);
		return dist(mt);
	}

	template<typename T>
	void shuffle(std::vector<T>& vec) {
		for (int i = 0; i < vec.size() - 1; ++i)
		{
			std::swap(vec[i], vec[randInt(vec.size() - i)]);
		}
	}
};

