import React, { useState, useEffect } from 'react';
import { Sprout, Droplets, Cloud, MessageCircle, Sun, Moon, Menu, X, ChevronUp, Leaf, Wind, ThermometerSun } from 'lucide-react';

export default function CropSafe() {
  const [theme, setTheme] = useState('light');
  const [activeTab, setActiveTab] = useState(0);
  const [showScrollTop, setShowScrollTop] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [chatMessages, setChatMessages] = useState([
    { sender: 'cropy', text: "Hello! I'm CroPy, your AI farming assistant. How can I help you today? 🌱" }
  ]);
  const [chatInput, setChatInput] = useState('');

  // Crop prediction states
  const [cropInputs, setCropInputs] = useState({
    nitrogen: 50,
    phosphorus: 50,
    potassium: 50,
    temperature: 25,
    humidity: 65,
    ph: 6.5,
    rainfall: 100
  });
  const [predictedCrop, setPredictedCrop] = useState(null);

  // Fertilizer states
  const [fertilizerInputs, setFertilizerInputs] = useState({
    crop: 'rice',
    nitrogen: 40,
    phosphorus: 40,
    potassium: 40
  });
  const [fertilizerRecommendation, setFertilizerRecommendation] = useState(null);

  const isDark = theme === 'dark';

  useEffect(() => {
    const handleScroll = () => {
      setShowScrollTop(window.scrollY > 300);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const features = [
    { icon: <Sprout className="w-8 h-8" />, title: 'Crop Prediction', desc: 'Get AI-based crop suggestions using soil and climate data.' },
    { icon: <Droplets className="w-8 h-8" />, title: 'Fertilizer Guide', desc: 'Discover the ideal fertilizer mix for your soil type and crop.' },
    { icon: <Cloud className="w-8 h-8" />, title: 'Weather Insights', desc: 'Access real-time weather forecasts and farm planning tools.' },
    { icon: <MessageCircle className="w-8 h-8" />, title: 'Chat with CroPy', desc: 'Ask CroPy about soil care, pest control, and seasonal tips.' }
  ];

  const predictCrop = () => {
    const crops = [
      { name: 'Rice', icon: '🌾', condition: cropInputs.rainfall > 150 && cropInputs.humidity > 60 },
      { name: 'Wheat', icon: '🌾', condition: cropInputs.temperature < 25 && cropInputs.rainfall < 100 },
      { name: 'Cotton', icon: '🌿', condition: cropInputs.temperature > 25 && cropInputs.potassium > 40 },
      { name: 'Sugarcane', icon: '🎋', condition: cropInputs.rainfall > 120 && cropInputs.nitrogen > 60 },
      { name: 'Maize', icon: '🌽', condition: cropInputs.ph > 6 && cropInputs.phosphorus > 40 },
      { name: 'Pulses', icon: '🫘', condition: cropInputs.nitrogen < 50 && cropInputs.ph > 6.5 }
    ];

    const suitable = crops.find(c => c.condition) || crops[Math.floor(Math.random() * crops.length)];
    setPredictedCrop(suitable);
  };

  const recommendFertilizer = () => {
    const recommendations = {
      rice: { type: 'Urea + DAP', ratio: '2:1:1', note: 'Apply in split doses' },
      wheat: { type: 'NPK Complex', ratio: '4:2:1', note: 'Best before seeding' },
      cotton: { type: 'Potash Rich', ratio: '1:2:3', note: 'Increase potassium' },
      maize: { type: 'Balanced NPK', ratio: '2:2:2', note: 'Every 3 weeks' },
      sugarcane: { type: 'High Nitrogen', ratio: '3:1:1', note: 'Multiple applications' }
    };

    const rec = recommendations[fertilizerInputs.crop] || recommendations.rice;
    setFertilizerRecommendation(rec);
  };

  const handleChatSend = () => {
    if (!chatInput.trim()) return;
    
    setChatMessages([...chatMessages, { sender: 'user', text: chatInput }]);
    
    setTimeout(() => {
      const responses = [
        "Great question! For pest control, I recommend neem oil spray as a natural solution. 🌿",
        "Based on your soil conditions, water deeply but less frequently to encourage strong root growth. 💧",
        "The best time for planting depends on your region. Generally, post-monsoon is ideal for most crops. 🌱",
        "Regular soil testing every 6 months helps optimize fertilizer use and crop yield! 🧪",
        "Consider crop rotation to maintain soil health and reduce pest buildup naturally. 🔄"
      ];
      setChatMessages(prev => [...prev, { 
        sender: 'cropy', 
        text: responses[Math.floor(Math.random() * responses.length)] 
      }]);
    }, 1000);
    
    setChatInput('');
  };

  return (
    <div className={`min-h-screen ${isDark ? 'bg-gradient-to-br from-gray-900 via-gray-800 to-green-900' : 'bg-gradient-to-br from-green-50 via-emerald-50 to-teal-50'} transition-all duration-500`}>
      {/* Header */}
      <header className={`${isDark ? 'bg-gray-800/90' : 'bg-white/90'} backdrop-blur-md shadow-lg sticky top-0 z-50`}>
        <div className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Sprout className={`w-8 h-8 ${isDark ? 'text-green-400' : 'text-green-600'}`} />
            <h1 className={`text-2xl font-bold ${isDark ? 'text-white' : 'text-gray-800'}`}>
              Crop<span className="text-green-500">Safe</span>
            </h1>
          </div>
          
          <div className="flex items-center gap-4">
            <button
              onClick={() => setTheme(isDark ? 'light' : 'dark')}
              className={`p-2 rounded-full ${isDark ? 'bg-gray-700 text-yellow-400' : 'bg-gray-100 text-gray-700'} hover:scale-110 transition-transform`}
            >
              {isDark ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
            </button>
            <button
              onClick={() => setSidebarOpen(!sidebarOpen)}
              className="lg:hidden p-2"
            >
              {sidebarOpen ? <X /> : <Menu />}
            </button>
          </div>
        </div>
      </header>

      {/* Welcome Section */}
      <div className="max-w-7xl mx-auto px-4 py-8">
        <div className={`${isDark ? 'bg-gray-800/70' : 'bg-white/70'} backdrop-blur-lg rounded-3xl p-8 shadow-2xl mb-8`}>
          <div className="flex flex-col md:flex-row items-center gap-6">
            <div className="w-32 h-32 bg-gradient-to-br from-green-400 to-emerald-600 rounded-full flex items-center justify-center animate-pulse">
              <Sprout className="w-16 h-16 text-white" />
            </div>
            <div className="flex-1 text-center md:text-left">
              <h2 className={`text-4xl font-bold mb-3 ${isDark ? 'text-white' : 'text-gray-800'}`}>
                Welcome to <span className="text-green-500">CropSafe</span> 🌾
              </h2>
              <p className={`text-lg ${isDark ? 'text-gray-300' : 'text-gray-600'}`}>
                👩‍🌾 Hello farmer! I'm <strong>CroPy</strong> — your AI-powered farming buddy 🤖
                <br />
                Let's make your farming smarter, sustainable, and more productive 🌱
              </p>
            </div>
          </div>
        </div>

        {/* Feature Cards */}
        <h3 className={`text-2xl font-bold mb-6 ${isDark ? 'text-white' : 'text-gray-800'}`}>
          🌟 Explore CroPy Features
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          {features.map((feature, idx) => (
            <div
              key={idx}
              className={`${isDark ? 'bg-gray-800/60' : 'bg-white/80'} backdrop-blur-sm rounded-2xl p-6 shadow-lg hover:shadow-2xl hover:-translate-y-2 transition-all duration-300 cursor-pointer text-center`}
              onClick={() => setActiveTab(idx)}
            >
              <div className={`inline-flex p-4 rounded-full ${isDark ? 'bg-green-900/50' : 'bg-green-100'} mb-4`}>
                {React.cloneElement(feature.icon, { className: `w-8 h-8 ${isDark ? 'text-green-400' : 'text-green-600'}` })}
              </div>
              <h4 className={`text-lg font-bold mb-2 ${isDark ? 'text-white' : 'text-gray-800'}`}>
                {feature.title}
              </h4>
              <p className={`text-sm ${isDark ? 'text-gray-400' : 'text-gray-600'}`}>
                {feature.desc}
              </p>
            </div>
          ))}
        </div>

        {/* Interactive Tabs */}
        <div className={`${isDark ? 'bg-gray-800/70' : 'bg-white/70'} backdrop-blur-lg rounded-3xl shadow-2xl overflow-hidden`}>
          <div className={`flex border-b ${isDark ? 'border-gray-700' : 'border-gray-200'} overflow-x-auto`}>
            {['🌾 Crop Prediction', '💧 Fertilizer', '🌦️ Weather', '💬 Chat'].map((tab, idx) => (
              <button
                key={idx}
                onClick={() => setActiveTab(idx)}
                className={`px-6 py-4 font-semibold whitespace-nowrap transition-all ${
                  activeTab === idx
                    ? `${isDark ? 'bg-green-900/50 text-green-400' : 'bg-green-50 text-green-600'} border-b-2 border-green-500`
                    : `${isDark ? 'text-gray-400 hover:bg-gray-700' : 'text-gray-600 hover:bg-gray-50'}`
                }`}
              >
                {tab}
              </button>
            ))}
          </div>

          <div className="p-8">
            {activeTab === 0 && (
              <div>
                <h3 className={`text-2xl font-bold mb-6 ${isDark ? 'text-white' : 'text-gray-800'}`}>
                  🌾 Crop Prediction
                </h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                  {Object.keys(cropInputs).map(key => (
                    <div key={key}>
                      <label className={`block text-sm font-medium mb-2 capitalize ${isDark ? 'text-gray-300' : 'text-gray-700'}`}>
                        {key}: {cropInputs[key]}
                      </label>
                      <input
                        type="range"
                        min={key === 'ph' ? 4 : key === 'temperature' ? 0 : 0}
                        max={key === 'ph' ? 9 : key === 'temperature' ? 45 : key === 'rainfall' ? 300 : 100}
                        step={key === 'ph' ? 0.1 : 1}
                        value={cropInputs[key]}
                        onChange={(e) => setCropInputs({...cropInputs, [key]: parseFloat(e.target.value)})}
                        className="w-full"
                      />
                    </div>
                  ))}
                </div>
                <button
                  onClick={predictCrop}
                  className="bg-green-600 hover:bg-green-700 text-white px-8 py-3 rounded-full font-semibold shadow-lg hover:shadow-xl transition-all"
                >
                  Predict Best Crop 🌱
                </button>
                {predictedCrop && (
                  <div className={`mt-6 p-6 ${isDark ? 'bg-green-900/30' : 'bg-green-50'} rounded-2xl border-2 border-green-500`}>
                    <h4 className={`text-xl font-bold ${isDark ? 'text-white' : 'text-gray-800'} mb-2`}>
                      Recommended Crop: {predictedCrop.icon} {predictedCrop.name}
                    </h4>
                    <p className={isDark ? 'text-gray-300' : 'text-gray-600'}>
                      Based on your soil and climate conditions, {predictedCrop.name} is the best choice!
                    </p>
                  </div>
                )}
              </div>
            )}

            {activeTab === 1 && (
              <div>
                <h3 className={`text-2xl font-bold mb-6 ${isDark ? 'text-white' : 'text-gray-800'}`}>
                  💧 Fertilizer Recommendation
                </h3>
                <div className="space-y-4 mb-6">
                  <div>
                    <label className={`block text-sm font-medium mb-2 ${isDark ? 'text-gray-300' : 'text-gray-700'}`}>
                      Select Crop
                    </label>
                    <select
                      value={fertilizerInputs.crop}
                      onChange={(e) => setFertilizerInputs({...fertilizerInputs, crop: e.target.value})}
                      className={`w-full p-3 rounded-lg ${isDark ? 'bg-gray-700 text-white' : 'bg-white text-gray-800'} border ${isDark ? 'border-gray-600' : 'border-gray-300'}`}
                    >
                      <option value="rice">Rice 🌾</option>
                      <option value="wheat">Wheat 🌾</option>
                      <option value="cotton">Cotton 🌿</option>
                      <option value="maize">Maize 🌽</option>
                      <option value="sugarcane">Sugarcane 🎋</option>
                    </select>
                  </div>
                  {['nitrogen', 'phosphorus', 'potassium'].map(nutrient => (
                    <div key={nutrient}>
                      <label className={`block text-sm font-medium mb-2 capitalize ${isDark ? 'text-gray-300' : 'text-gray-700'}`}>
                        {nutrient} Level: {fertilizerInputs[nutrient]}
                      </label>
                      <input
                        type="range"
                        min="0"
                        max="100"
                        value={fertilizerInputs[nutrient]}
                        onChange={(e) => setFertilizerInputs({...fertilizerInputs, [nutrient]: parseInt(e.target.value)})}
                        className="w-full"
                      />
                    </div>
                  ))}
                </div>
                <button
                  onClick={recommendFertilizer}
                  className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-full font-semibold shadow-lg hover:shadow-xl transition-all"
                >
                  Get Recommendation 🧪
                </button>
                {fertilizerRecommendation && (
                  <div className={`mt-6 p-6 ${isDark ? 'bg-blue-900/30' : 'bg-blue-50'} rounded-2xl border-2 border-blue-500`}>
                    <h4 className={`text-xl font-bold ${isDark ? 'text-white' : 'text-gray-800'} mb-2`}>
                      Recommended: {fertilizerRecommendation.type}
                    </h4>
                    <p className={`${isDark ? 'text-gray-300' : 'text-gray-600'} mb-2`}>
                      <strong>NPK Ratio:</strong> {fertilizerRecommendation.ratio}
                    </p>
                    <p className={isDark ? 'text-gray-400' : 'text-gray-500'}>
                      💡 {fertilizerRecommendation.note}
                    </p>
                  </div>
                )}
              </div>
            )}

            {activeTab === 2 && (
              <div>
                <h3 className={`text-2xl font-bold mb-6 ${isDark ? 'text-white' : 'text-gray-800'}`}>
                  🌦️ Weather Insights
                </h3>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                  <div className={`${isDark ? 'bg-blue-900/30' : 'bg-blue-50'} p-6 rounded-2xl text-center`}>
                    <ThermometerSun className={`w-12 h-12 mx-auto mb-3 ${isDark ? 'text-blue-400' : 'text-blue-600'}`} />
                    <h4 className={`text-lg font-bold ${isDark ? 'text-white' : 'text-gray-800'}`}>Temperature</h4>
                    <p className={`text-3xl font-bold ${isDark ? 'text-blue-400' : 'text-blue-600'}`}>28°C</p>
                  </div>
                  <div className={`${isDark ? 'bg-cyan-900/30' : 'bg-cyan-50'} p-6 rounded-2xl text-center`}>
                    <Droplets className={`w-12 h-12 mx-auto mb-3 ${isDark ? 'text-cyan-400' : 'text-cyan-600'}`} />
                    <h4 className={`text-lg font-bold ${isDark ? 'text-white' : 'text-gray-800'}`}>Humidity</h4>
                    <p className={`text-3xl font-bold ${isDark ? 'text-cyan-400' : 'text-cyan-600'}`}>72%</p>
                  </div>
                  <div className={`${isDark ? 'bg-purple-900/30' : 'bg-purple-50'} p-6 rounded-2xl text-center`}>
                    <Wind className={`w-12 h-12 mx-auto mb-3 ${isDark ? 'text-purple-400' : 'text-purple-600'}`} />
                    <h4 className={`text-lg font-bold ${isDark ? 'text-white' : 'text-gray-800'}`}>Wind Speed</h4>
                    <p className={`text-3xl font-bold ${isDark ? 'text-purple-400' : 'text-purple-600'}`}>12 km/h</p>
                  </div>
                </div>
                <div className={`mt-6 p-6 ${isDark ? 'bg-gray-700' : 'bg-gray-100'} rounded-2xl`}>
                  <p className={`text-center ${isDark ? 'text-gray-300' : 'text-gray-700'}`}>
                    ☀️ Perfect conditions for irrigation today! Plan your watering schedule accordingly.
                  </p>
                </div>
              </div>
            )}

            {activeTab === 3 && (
              <div>
                <h3 className={`text-2xl font-bold mb-6 ${isDark ? 'text-white' : 'text-gray-800'}`}>
                  💬 Chat with CroPy
                </h3>
                <div className={`${isDark ? 'bg-gray-700/50' : 'bg-gray-50'} rounded-2xl p-4 h-96 overflow-y-auto mb-4`}>
                  {chatMessages.map((msg, idx) => (
                    <div key={idx} className={`mb-4 flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
                      <div className={`max-w-[70%] p-4 rounded-2xl ${
                        msg.sender === 'user'
                          ? 'bg-green-600 text-white rounded-tr-none'
                          : `${isDark ? 'bg-gray-600 text-white' : 'bg-white text-gray-800'} rounded-tl-none shadow`
                      }`}>
                        {msg.text}
                      </div>
                    </div>
                  ))}
                </div>
                <div className="flex gap-2">
                  <input
                    type="text"
                    value={chatInput}
                    onChange={(e) => setChatInput(e.target.value)}
                    onKeyPress={(e) => e.key === 'Enter' && handleChatSend()}
                    placeholder="Ask CroPy anything..."
                    className={`flex-1 p-3 rounded-full ${isDark ? 'bg-gray-700 text-white' : 'bg-white text-gray-800'} border ${isDark ? 'border-gray-600' : 'border-gray-300'}`}
                  />
                  <button
                    onClick={handleChatSend}
                    className="bg-green-600 hover:bg-green-700 text-white px-6 py-3 rounded-full font-semibold shadow-lg transition-all"
                  >
                    Send
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Footer */}
        <div className={`mt-12 text-center p-8 ${isDark ? 'bg-gray-800/50' : 'bg-white/50'} backdrop-blur-sm rounded-3xl`}>
          <h3 className={`text-2xl font-bold mb-3 ${isDark ? 'text-white' : 'text-gray-800'}`}>
            🤖 About CroPy
          </h3>
          <p className={`${isDark ? 'text-gray-300' : 'text-gray-600'} mb-2`}>
            CroPy is your AI-powered farming assistant, offering data-driven insights
            <br />
            for crops, fertilizers, and weather management 🌱
          </p>
          <p className={`font-semibold ${isDark ? 'text-gray-400' : 'text-gray-700'}`}>
            © 2025 CropSafe | Built with ❤️ by <strong>CroPy</strong> 🤖
          </p>
        </div>
      </div>

      {/* Scroll to Top Button */}
      {showScrollTop && (
        <button
          onClick={scrollToTop}
          className="fixed bottom-6 right-6 bg-green-600 hover:bg-green-700 text-white p-4 rounded-full shadow-2xl hover:scale-110 transition-all z-50"
        >
          <ChevronUp className="w-6 h-6" />
        </button>
      )}
    </div>
  );
}