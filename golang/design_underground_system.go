package main

import "fmt"

type UndergroundSystem struct {
	SourceMap     map[int]string
	SourceTimeMap map[int]int
	CountMap      map[string]int
	AverageMap    map[string]float64
}

func UndergroundSystemConstructor() UndergroundSystem {
	return UndergroundSystem{
		SourceMap:     map[int]string{},
		SourceTimeMap: map[int]int{},
		CountMap:      map[string]int{},
		AverageMap:    map[string]float64{},
	}
}

func (this *UndergroundSystem) CheckIn(id int, stationName string, t int) {
	this.SourceMap[id] = stationName
	this.SourceTimeMap[id] = t
}

func (this *UndergroundSystem) CheckOut(id int, stationName string, t int) {
	source := this.SourceMap[id]
	sourceTime := this.SourceTimeMap[id]
	travelTime := float64(t - sourceTime)

	keyStr := sourceDestinationString(source, stationName)
	if _, ok := this.AverageMap[keyStr]; ok {
		currAvg := this.AverageMap[keyStr]
		count := this.CountMap[keyStr]

		this.AverageMap[keyStr] = ((currAvg * float64(count)) + travelTime) / float64(count+1)
		this.CountMap[keyStr]++
	} else {
		this.AverageMap[keyStr] = travelTime
		this.CountMap[keyStr] = 1
	}
}

func (this *UndergroundSystem) GetAverageTime(startStation string, endStation string) float64 {
	return this.AverageMap[sourceDestinationString(startStation, endStation)]
}

func sourceDestinationString(source string, destination string) string {
	return fmt.Sprintf("%s-%s", source, destination)
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * obj := Constructor();
 * obj.CheckIn(id,stationName,t);
 * obj.CheckOut(id,stationName,t);
 * param_3 := obj.GetAverageTime(startStation,endStation);
 */
