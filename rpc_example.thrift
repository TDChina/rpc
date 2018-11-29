namespace py example

service example{
	string ping(),
	string hello(1: string name),
	double add(1: double numberA, 2: double numberB)
}