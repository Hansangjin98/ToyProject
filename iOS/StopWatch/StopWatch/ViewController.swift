//
//  ViewController.swift
//  StopWatch
//
//  Created by 한상진 on 2021/01/14.
//

import UIKit

class ViewController: UIViewController, UITableViewDelegate {
    
    @IBOutlet var lblIntervalTime: UILabel!
    @IBOutlet var lblCurrentTime: UILabel!
    @IBOutlet var btnLapReset: UIButton!
    @IBOutlet var btnStartStop: UIButton!
    @IBOutlet var tvListView: UITableView!
    
    var state: Bool = false
    var mainTimer = Timer()
    var subTimer = Timer()
    var (mainHours, mainMinutes, mainSeconds, mainCount) = (0, 0, 0, 0)
    var (subHours, subMinutes, subSeconds, subCount) = (0, 0, 0, 0)
    var lapList: [String?] = []
    var timeList: [String?] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    @IBAction func btnLapResetTouched(_ sender: UIButton) {
        if (state == true) {
            lapList.insert("Lap " + "\(lapList.count + 1)", at: 0)
            timeList.insert(lblCurrentTime.text, at: 0)
            tvListView.reloadData()
            (subHours, subMinutes, subSeconds, subCount) = (0, 0, 0, 0)
        } else {
            lapList.removeAll()
            timeList.removeAll()
            (mainHours, mainMinutes, mainSeconds, mainCount) = (0, 0, 0, 0)
            (subHours, subMinutes, subSeconds, subCount) = (0, 0, 0, 0)
            lblIntervalTime.text = "00:00:00.00"
            lblCurrentTime.text = "00:00:00.00"
            tvListView.reloadData()
            btnLapReset.setTitle("Lap", for: .normal)
        }
    }
    
    @IBAction func btnStartStopTouched(_ sender: UIButton) {
        if (state == false) {
            state = true
            btnStartStop.setTitle("Stop", for: .normal)
            btnLapReset.setTitle("Lap", for: .normal)
            btnStartStop.setTitleColor(UIColor.red, for: .normal)
            mainTimer = Timer.scheduledTimer(timeInterval: 0.01, target: self, selector: #selector(ViewController.updateMainTimer), userInfo: nil, repeats: true)
            subTimer = Timer.scheduledTimer(timeInterval: 0.01, target: self, selector: #selector(ViewController.updateSubTimer), userInfo: nil, repeats: true)
        } else {
            state = false
            btnStartStop.setTitle("Start", for: .normal)
            btnLapReset.setTitle("Reset", for: .normal)
            btnStartStop.setTitleColor(UIColor.green, for: .normal)
            mainTimer.invalidate()
            subTimer.invalidate()
        }
    }
    
    @objc func updateMainTimer() {
        mainCount += 1
        if (mainCount > 99) {
            mainSeconds += 1
            mainCount = 0
        }
        if (mainSeconds == 60) {
            mainMinutes += 1
            mainSeconds = 00
        }
        if (mainMinutes == 60) {
            mainHours += 1
            mainMinutes = 00
        }
        let countString = mainCount > 9 ? "\(mainCount)" : "0\(mainCount)"
        let secondString = mainSeconds > 9 ? "\(mainSeconds)" : "0\(mainSeconds)"
        let minutesString = mainMinutes > 9 ? "\(mainMinutes)" : "0\(mainMinutes)"
        let hoursString = mainHours > 9 ? "\(mainHours)" : "0\(mainHours)"
        
        lblCurrentTime.text = "\(hoursString):\(minutesString):\(secondString).\(countString)"
    }
    
    @objc func updateSubTimer() {
        subCount += 1
        if (subCount > 99) {
            subSeconds += 1
            subCount = 0
        }
        if (subSeconds == 60) {
            subMinutes += 1
            subSeconds = 00
        }
        if (subMinutes == 60) {
            subHours += 1
            subMinutes = 00
        }
        let countString = subCount > 9 ? "\(subCount)" : "0\(subCount)"
        let secondString = subSeconds > 9 ? "\(subSeconds)" : "0\(subSeconds)"
        let minutesString = subMinutes > 9 ? "\(subMinutes)" : "0\(subMinutes)"
        let hoursString = subHours > 9 ? "\(subHours)" : "0\(subHours)"
        
        lblIntervalTime.text = "\(hoursString):\(minutesString):\(secondString).\(countString)"
    }
}

extension ViewController: UITableViewDataSource {
    
    func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return lapList.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "myCell", for: indexPath)

        cell.textLabel?.text = lapList[indexPath.row]
        cell.detailTextLabel?.text = timeList[indexPath.row]

        return cell
    }
}

