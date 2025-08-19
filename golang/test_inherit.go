package main

import (
	"fmt"
	"time"
)

var OSMap = map[string]Printable{
	"Windows10": Windows{OS: OS{Name: "Windows 10", IsFree: false}, SupportedDate: time.Now()},
	"Ubuntu":    Linux{OS: OS{Name: "Ubuntu", IsFree: true}, IsAptBased: true},
}

type Printable interface {
	PrintStats()
}

type OS struct {
	Name   string
	IsFree bool
}

func (o OS) PrintStats() {
	fmt.Println(o.Name)
	fmt.Println(o.IsFree)
}

type Windows struct {
	OS
	SupportedDate time.Time
}

func (o Windows) PrintStats() {
	o.OS.PrintStats()
	fmt.Println(o.SupportedDate)
}

type Linux struct {
	OS
	IsAptBased bool
	IsYumBased bool
}

func (o Linux) PrintStats() {
	o.OS.PrintStats()
	fmt.Println(o.IsAptBased)
	fmt.Println(o.IsYumBased)
}

func GetFunc(name string) {
	if _, ok := OSMap[name]; ok {
		OSMap[name].PrintStats()
	}
}

func main() {
	GetFunc("Windows10")
	GetFunc("Ubuntu")
}
