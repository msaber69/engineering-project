// Structure: { id: 'Q1', text: 'How often...', options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'] }
const questions = [
    // Test 1: Mental Health Assessment
    {
      id: 'Q1',
      text: 'How often do you have trouble wrapping up the final details of a project, once the challenging parts have been done?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test1',
    },
    {
      id: 'Q2',
      text: 'How often do you have difficulty getting things in order when you have to do a task that requires organization?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test1',
    },
    {
      id: 'Q3',
      text: 'How often do you have problems remembering appointments or obligations?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test1',
    },
    {
      id: 'Q4',
      text: 'When you have a task that requires a lot of thought, how often do you avoid or delay getting started?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test1',
    },
    {
      id: 'Q5',
      text: 'How often do you fidget or squirm with your hands or feet when you have to sit down for a long time?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test1',
    },
    {
      id: 'Q6',
      text: 'How often do you feel overly active and compelled to do things, like you were driven by a motor?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
    },
    {
      id: 'Q7',
      text: 'How often do you make careless mistakes when you have to work on a boring or difficult project?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test1',
    },
    {
      id: 'Q8',
      text: 'How often do you have difficulty keeping your attention when you are doing boring or repetitive work?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test1',
    },
    {
      id: 'Q9',
      text: 'How often do you have difficulty concentrating on what people say to you, even when they are speaking to you directly?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test1',
    },
    {
      id: 'Q10',
      text: 'How often do you misplace or have difficulty finding things at home or at work?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test1',
    },
    {
      id: 'Q11',
      text: 'How often are you distracted by activity or noise around you?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test1',
    },
    {
      id: 'Q12',
      text: 'How often do you leave your seat in meetings or other situations in which you are expected to remain seated?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test1',
    },
    {
      id: 'Q13',
      text: 'How often do you feel restless or fidgety?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test1',
    },
    {
      id: 'Q14',
      text: 'How often do you have difficulty unwinding and relaxing when you have time to yourself?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test1',
    },
    {
      id: 'Q15',
      text: 'How often do you find yourself talking too much when you are in social situations?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test1',
    },
    {
      id: 'Q16',
      text: 'When you’re in a conversation, how often do you find yourself finishing the sentences of the people you are talking to, before they can finish them themselves?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test1',
    },
    {
      id: 'Q17',
      text: 'How often do you have difficulty waiting your turn in situations when turn taking is required?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test1',
    },
  
    // Test 2: ADHD/ADD
    {
      id: 'Q18',
      text: 'During the past TWO (2) WEEKS, how much (or how often) have you been bothered by the following problems?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test2',
    },
    {
      id: 'Q19',
      text: 'Little interest or pleasure in doing things?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test2',
    },
    {
      id: 'Q20',
      text: 'Feeling down, depressed, or hopeless?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test2',
    },
    {
      id: 'Q21',
      text: 'Feeling more irritated, grouchy, or angry than usual?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test2',
    },
    {
      id: 'Q22',
      text: 'Sleeping less than usual, but still have a lot of energy?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test2',
    },
    {
      id: 'Q23',
      text: 'Starting lots more projects than usual or doing more risky things than usual?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test2',
    },
    {
      id: 'Q24',
      text: 'Feeling nervous, anxious, frightened, worried, or on edge?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test2',
    },
    {
      id: 'Q25',
      text: 'Feeling panic or being frightened?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test2',
    },
    {
      id: 'Q26',
      text: 'Avoiding situations that make you anxious?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test2',
    },
    {
      id: 'Q27',
      text: 'Unexplained aches and pains (e.g., headaches, backaches, stomachaches)?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test2',
    },
    {
      id: 'Q28',
      text: 'Feeling suddenly scared for no reason?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test2',
    },
    {
      id: 'Q29',
      text: 'Feeling that something bad is going to happen (e.g., your heart is going to stop, you\'re going to choke, faint, have a heart attack, or "go crazy")?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test2',
    },
    {
      id: 'Q30',
      text: 'Pounding or racing heart or having trouble breathing?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test2',
    },
    {
      id: 'Q31',
      text: 'Having nightmares about the traumatic event(s) that you experienced?',
      options: ['Never', 'Rarely', 'Sometimes', 'Often', 'Very Often'],
      section: 'Test2',
    },
    {
      id: 'Q32',
      text: 'How much are you bothered by the following symptoms?',
      options: ['Not at all', 'A little bit', 'Moderately', 'Quite a bit', 'Extremely'],
      section: 'Test2',
    },
    {
      id: 'Q33',
      text: 'Upsetting thoughts or memories about a stressful experience from the past that you cannot get out of your mind?',
      options: ['Not at all', 'A little bit', 'Moderately', 'Quite a bit', 'Extremely'],
      section: 'Test2',
    },
    {
      id: 'Q34',
      text: 'Loss of interest or pleasure in activities that you used to enjoy?',
      options: ['Not at all', 'A little bit', 'Moderately', 'Quite a bit', 'Extremely'],
      section: 'Test2',
    },
    {
      id: 'Q35',
      text: 'Feeling distant or cut off from other people?',
      options: ['Not at all', 'A little bit', 'Moderately', 'Quite a bit', 'Extremely'],
      section: 'Test2',
    },
    {
      id: 'Q36',
      text: 'Feeling irritable or having angry outbursts?',
      options: ['Not at all', 'A little bit', 'Moderately', 'Quite a bit', 'Extremely'],
      section: 'Test2',
    },
    {
      id: 'Q37',
      text: 'Having difficulty concentrating or making decisions?',
      options: ['Not at all', 'A little bit', 'Moderately', 'Quite a bit', 'Extremely'],
      section: 'Test2',
    },
    {
      id: 'Q38',
      text: 'Trouble falling or staying asleep, or restless and unsatisfying sleep?',
      options: ['Not at all', 'A little bit', 'Moderately', 'Quite a bit', 'Extremely'],
      section: 'Test2',
    },
    {
      id: 'Q39',
      text: 'Feeling very nervous or on edge?',
      options: ['Not at all', 'A little bit', 'Moderately', 'Quite a bit', 'Extremely'],
      section: 'Test2',
    },
  
    // Test 3: Depression
    {
      id: 'Q40',
      text: 'Over the last two weeks, how often have you experienced the following problems?',
      section: 'Test3',
    },
    {
      id: 'Q41',
      text: 'Little interest or pleasure in doing things?',
      options: ['Not at all', 'Several days', 'More than half the days', 'Nearly every day'],
      section: 'Test3',
    },
    {
      id: 'Q42',
      text: 'Feeling down, depressed, or hopeless?',
      options: ['Not at all', 'Several days', 'More than half the days', 'Nearly every day'],
      section: 'Test3',
    },
    {
      id: 'Q43',
      text: 'Trouble falling or staying asleep, or sleeping too much?',
      options: ['Not at all', 'Several days', 'More than half the days', 'Nearly every day'],
      section: 'Test3',
    },
    {
      id: 'Q44',
      text: 'Feeling tired or having little energy?',
      options: ['Not at all', 'Several days', 'More than half the days', 'Nearly every day'],
      section: 'Test3',
    },
    {
      id: 'Q45',
      text: 'Poor appetite or overeating?',
      options: ['Not at all', 'Several days', 'More than half the days', 'Nearly every day'],
      section: 'Test3',
    },
    {
      id: 'Q46',
      text: 'Feeling bad about yourself or that you are a failure or have let yourself or your family down?',
      options: ['Not at all', 'Several days', 'More than half the days', 'Nearly every day'],
      section: 'Test3',
    },
    {
      id: 'Q47',
      text: 'Trouble concentrating on things, such as reading the newspaper or watching television?',
      options: ['Not at all', 'Several days', 'More than half the days', 'Nearly every day'],
      section: 'Test3',
    },
    {
      id: 'Q48',
      text: 'Moving or speaking so slowly that other people could have noticed, or the opposite – being so fidgety or restless that you have been moving around a lot more than usual?',
      options: ['Not at all', 'Several days', 'More than half the days', 'Nearly every day'],
      section: 'Test3',
    },
    {
      id: 'Q49',
      text: 'Thoughts that you would be better off dead or of hurting yourself in some way?',
      options: ['Not at all', 'Several days', 'More than half the days', 'Nearly every day'],
      section: 'Test3',
    },
  ];

  
export default questions;  