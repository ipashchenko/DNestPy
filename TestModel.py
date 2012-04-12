from Model import *
import numpy as np
import numpy.random as rng

class TestModel(Model):
	def __init__(self):
		Model.__init__(self)
		self.params = np.zeros(20)

	def fromPrior(self):
		self.params = -0.5 + rng.rand(self.params.size)		
		Model.fromPrior(self)
		self.calculateLogLikelihood()

	def perturb(self):
		logH = 0.0
		which = rng.randint(self.params.size)
		self.params[which] += 10.0**(1.5 - 6.0*rng.rand())*rng.randn()
		self.params[which] = np.mod(self.params[which] + 0.5,\
					1.0) - 0.5
		logH += Model.perturb(self)
		self.calculateLogLikelihood()
		return logH

	def calculateLogLikelihood(self):
		self.logl[0] = -0.5*np.sum((self.params/0.01)**2)

	def __str__(self):
		return "".join(str(i) + " " for i in self.params)

if __name__ == '__main__':
	from Level import *
	l = Level()
	t = TestModel()
	t.fromPrior()
	for i in xrange(0, 1000):
		t = t.update(l)
		print(str(t))

