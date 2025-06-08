package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"net/url"
	"os"
	"sort"
)

const (
	GetHotelURL     string = "https://challenge-server.tracks.run/hotel-reservation-en/hotels"
	ReserveHotelURL string = "https://challenge-server.tracks.run/hotel-reservation-en/reservations"
)

type ReservationRequest struct {
	Keyword    string   `json:"keyword"`
	CheckIn    string   `json:"checkin"`
	CheckOut   string   `json:"checkout"`
	Number     int      `json:"number"`
	Conditions []string `json:"condition"`
}

type GetHotelResponse struct {
	ID         int         `json:"keyword"`
	Name       string      `json:"name"`
	Prefecture int         `json:"prefecture"`
	Address    string      `json:"address"`
	Conditions []string    `json:"conditions"`
	Rooms      []HotelRoom `json:"rooms"`
	Plans      []HotelPlan `json:"plans"`
}

type HotelRoom struct {
	ID         int      `json:"id"`
	Name       string   `json:"name"`
	Capacity   int      `json:"capacity"`
	Count      int      `json:"count"`
	Conditions []string `json:"conditions"`
}

type HotelPlan struct {
	ID         int      `json:"id"`
	Name       string   `json:"name"`
	RoomID     int      `json:"room_id"`
	Price      int      `json:"price"`
	Conditions []string `json:"conditions"`

	hotelID int `json:"-"`
	roomID  int `json:"-"`
}

type ReserveHotelRequest struct {
	CheckIn  string `json:"checkin"`
	CheckOut string `json:"checkout"`
	PlanID   int    `json:"plan_id"`
	Number   int    `json:"number"`
}

type ReserveHotelResponse struct {
	ID       int    `json:"id"`
	CheckIn  string `json:"checkin"`
	CheckOut string `json:"checkout"`
	PlanID   int    `json:"plan_id"`
	Number   int    `json:"number"`
}

func main() {
	// This is sample code to use command line arguments and stdout.
	// Edit or remove this code as you like.

	token, req, err := parseRequest(os.Args[1:])
	if err != nil {
		log.Fatalln(err)
		return
	}

	hotelResponses, err := getHotel(token, req)
	if err != nil {
		log.Fatalln(err)
		return
	}

	if len(hotelResponses) == 0 {
		fmt.Println("Plan not found.")
	}

	hotelMap := make(map[int]string)
	roomMap := make(map[int]string)

	plans := []HotelPlan{}
	for _, hotel := range hotelResponses {
		hotelMap[hotel.ID] = hotel.Name

		for _, room := range hotel.Rooms {
			roomMap[room.ID] = room.Name
		}

		for _, plan := range hotel.Plans {
			plan.hotelID = hotel.ID
			plans = append(plans, plan)
		}
	}

	sort.Slice(plans, func(i, j int) bool {
		// sort by price
		if plans[i].Price != plans[j].Price {
			return plans[i].Price < plans[j].Price
		}
		// sort by ID
		return plans[i].ID < plans[j].ID
	})

	chosenPlan := plans[0]
	reserveHotelReq := ReserveHotelRequest{
		CheckIn:  req.CheckIn,
		CheckOut: req.CheckOut,
		PlanID:   chosenPlan.ID,
		Number:   req.Number,
	}

	reserveHotelResp, err := reserveHotel(token, reserveHotelReq)
	if err != nil {
		fmt.Println("Cheapest plan is fully booked.")
		return
	}

	fmt.Printf("The cheapest plan has been successfully reserved.\n")
	fmt.Printf("- reservation id: %d\n", reserveHotelResp.ID)
	fmt.Printf("- hotel name: %s\n", hotelMap[chosenPlan.hotelID])
	fmt.Printf("- room name: %s\n", roomMap[chosenPlan.roomID])
	fmt.Printf("- total price: %d\n", reserveHotelReq.Number*chosenPlan.Price)
}

func getHotel(token string, request ReservationRequest) ([]GetHotelResponse, error) {
	url, err := url.Parse(GetHotelURL)
	if err != nil {
		panic(err)
	}

	q := url.Query()
	q.Set("keyword", request.Keyword)
	q.Set("checkin", request.CheckIn)
	q.Set("checkout", request.CheckOut)
	for _, condition := range request.Conditions {
		q.Add("condition", condition)
	}
	url.RawQuery = q.Encode()

	req, err := http.NewRequest("GET", url.String(), nil)
	if err != nil {
		return nil, err
	}

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("X-ACCESS-TOKEN", token)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	var responses []GetHotelResponse
	err = json.NewDecoder(resp.Body).Decode(&responses)
	if err != nil {
		return nil, err
	}

	return responses, nil
}

func reserveHotel(token string, request ReserveHotelRequest) (ReserveHotelResponse, error) {
	// Marshal struct to JSON
	jsonData, err := json.Marshal(request)
	if err != nil {
		panic(err)
	}

	// Create HTTP request
	req, err := http.NewRequest("POST", ReserveHotelURL, bytes.NewBuffer(jsonData))
	if err != nil {
		panic(err)
	}

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("X-ACCESS-TOKEN", token)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return ReserveHotelResponse{}, err
	}
	defer resp.Body.Close()

	var response ReserveHotelResponse
	err = json.NewDecoder(resp.Body).Decode(&response)
	if err != nil {
		return ReserveHotelResponse{}, err
	}

	return response, nil
}

func parseRequest(args []string) (string, ReservationRequest, error) {
	accessToken := args[0]
	requestString := args[1]

	var req ReservationRequest
	if err := json.Unmarshal([]byte(requestString), &req); err != nil {
		return "", ReservationRequest{}, err
	}

	return accessToken, req, nil
}
